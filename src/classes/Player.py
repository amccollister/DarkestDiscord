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

    def level_up(self, column):
        self.bot.db.update_row("PLAYERS", "{0} = {0} + 1".format(column), "playerID = {}"
                               .format(self.player_id))
        return "Increased {} by 1".format(column)

    def add_resources(self, column, amount):
        self.bot.db.update_row("PLAYERS", "{0} = {0} + {1}".format(column, amount), "playerID = {}"
                               .format(self.player_id))
        return "Increased {} by {}".format(column, amount)
