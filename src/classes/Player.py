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

    @staticmethod
    def add_players(bot):
        id_list = [u.id for u in bot.users]
        bot.cur.execute("BEGIN TRANSACTION")  # begin trans and commit is very important
        for uid in id_list:
            bot.cur.execute("INSERT OR IGNORE INTO PLAYERS (playerID) VALUES({})".format(uid))
        bot.cur.execute("COMMIT")
        bot.con.commit()

    def get_player_info(self):
        self.bot.cur.execute("INSERT OR IGNORE INTO PLAYERS (playerID) VALUES({})".format(self.player_id))
        self.bot.cur.execute("SELECT * FROM PLAYERS WHERE playerID = {}".format(self.player_id))
        player = self.bot.cur.fetchone()
        return player

    def level_up(self, column):
        self.bot.cur.execute("UPDATE PLAYERS SET {0} = {0} + 1 WHERE playerID = {1}".format(column, self.player_id))
        user = self.bot.get_user(self.player_id)
        return "Increased {}'s {} by one.".format(user.name, column)

    def add_resources(self, column, amount):
        self.bot.cur.execute("UPDATE PLAYERS SET {0} = {0} + {1} WHERE playerID = {2}".format(column, amount, self.player_id))
        user = self.bot.get_user(self.player_id)
        return "Increased {}'s {} by {}.".format(user.name, column, amount)
