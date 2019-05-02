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

    def hire_adventurer(self, stagecoach_adv):
        stagecoach_id = stagecoach_adv["stagecoachID"]
        adv_id = stagecoach_adv["advID"]
        if not self.bot.db.get_row("STAGECOACH", "stagecoachID", stagecoach_id):
            return "The adventurer is no longer available."
        self.bot.db.delete_rows("STAGECOACH", "stagecoachID = {}".format(stagecoach_id))
        name = self.bot.db.get_row("ADVENTURER_LIST", "advID", adv_id)["name"]
        column = ["advID", "playerID", "level", "character_name"]
        values = [adv_id, self.player_id, stagecoach_adv["level"], name]
        self.bot.db.insert_row("ADVENTURERS", column, values)
        return "HIRED: Level {} {}".format(stagecoach_adv["level"], name)

    def level_up(self, column):
        self.bot.cur.execute("UPDATE PLAYERS SET {0} = {0} + 1 WHERE playerID = {1}".format(column, self.player_id))
        user = self.bot.get_user(self.player_id)
        return "Increased {}'s {} by one.".format(user.name, column)

    def add_resources(self, column, amount):
        self.bot.cur.execute("UPDATE PLAYERS SET {0} = {0} + {1} WHERE playerID = {2}".format(column, amount, self.player_id))
        user = self.bot.get_user(self.player_id)
        return "Increased {}'s {} by {}.".format(user.name, column, amount)
