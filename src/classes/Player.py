import src.constants as constants
from src.classes.Stagecoach import Stagecoach
from src.classes.Adventurer import Adventurer
# TODO: set info variable as the info and update the variable when anything changes


class Player(object):
    def __init__(self, bot, player_id):
        self.bot = bot
        self.player_id = player_id
        self.info = self.get_player_info()
        self.roster = self.get_roster()
        self.stagecoach = Stagecoach(bot, self)

    def update_info(self):
        self.__init__(self.bot, self.player_id)

    def get_player_info(self):
        self.bot.db.insert_row("PLAYERS", ["playerID"], [self.player_id])
        return self.bot.db.get_row("PLAYERS", "playerID", self.player_id)

    def get_roster(self):
        heroes = self.bot.db.get_rows("ADVENTURERS", "playerID", self.player_id)
        return [Adventurer(self.bot, hero["heroID"], self.player_id) for hero in heroes]

    def get_roster_cap(self):
        return constants.ADVENTURER_BASE_CAPACITY + self.info["roster_size_level"]

    def get_adventurer(self):
        pass

    def level_up(self, column):
        self.bot.db.update_row("PLAYERS", "{0} = {0} + 1".format(column), "playerID = {}"
                               .format(self.player_id))
        self.update_info()
        return "Increased {} by 1".format(column)

    def add_resource(self, column, amount):
        self.bot.db.update_row("PLAYERS", "{0} = {0} + {1}".format(column, amount), "playerID = {}"
                               .format(self.player_id))
        self.update_info()
        return "Increased {} by {}".format(column, amount)

    def hire(self, stagecoach_hire):
        if len(self.bot.db.get_rows("ADVENTURERS", "playerID", self.player_id)) >= self.get_roster_cap():
            return False
        stagecoach_id = stagecoach_hire["stagecoachID"]
        adv_id = stagecoach_hire["advID"]
        self.bot.db.delete_rows("STAGECOACH", "stagecoachID = {}".format(stagecoach_id))
        adv_class = self.stagecoach.get_class_row(adv_id)
        hp = adv_class["max_hp"] + stagecoach_hire["level"] * constants.LEVEL_UP["max_hp"]
        columns = ["advID", "playerID", "level", "hp", "name"]
        values = [adv_id, self.player_id, stagecoach_hire["level"], hp, stagecoach_hire["name"]]
        self.bot.db.insert_row("ADVENTURERS", columns, values)
        return True

    def fire(self, fired_hero):
        if not fired_hero.get_adventurer_info():
            return False
        self.bot.db.delete_rows("ADVENTURERS", "heroID = {}".format(fired_hero.info["heroID"]))
        self.update_info()
        return True
