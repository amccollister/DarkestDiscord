import src.constants as constants
from src.classes.Stagecoach import Stagecoach
# TODO: set info variable as the info and update the variable when anything changes
# TODO: use this class to add a player if they don't exist (dingus)
# TODO: store the stagecoach and roster in the player class


class Player(object):
    def __init__(self, bot, player_id):
        self.bot = bot
        self.player_id = player_id
        self.info = self.get_player_info()
        self.stagecoach = Stagecoach(bot, self)

    def get_player_info(self):
        self.bot.db.insert_row("PLAYERS", ["playerID"], [self.player_id])
        return self.bot.db.get_row("PLAYERS", "playerID", self.player_id)

    def get_roster_cap(self):
        return constants.ADVENTURER_BASE_CAPACITY + self.info["roster_level"]

    def hire_adventurer(self, stagecoach_hire):
        stagecoach_id = stagecoach_hire["stagecoachID"]
        adv_id = stagecoach_hire["advID"]
        if len(self.bot.db.get_rows("ADVENTURERS", "playerID", self.player_id)) >= self.get_roster_cap():
            return False
        self.bot.db.delete_rows("STAGECOACH", "stagecoachID = {}".format(stagecoach_id))
        name = self.stagecoach.get_class(adv_id)
        columns = ["advID", "playerID", "level", "character_name"]
        values = [adv_id, self.player_id, stagecoach_hire["level"], name]
        self.bot.db.insert_row("ADVENTURERS", columns, values)
        return True

    def level_up(self, column):
        pass

    def add_resources(self, column, amount):
        pass
