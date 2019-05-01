import random
import src.constants as constants

from datetime import datetime
# TODO: Code this better I think


class Stagecoach(object):
    def __init__(self, bot, player):
        self.bot = bot
        self.player = player
        self.adventurers = self.check_stagecoach(player.info)

    @staticmethod
    def refresh_stagecoach(bot):
        now = datetime.now()
        bot.cur.execute("SELECT * FROM STAGECOACH")
        heroes_before = len(bot.cur.fetchall())
        bot.cur.execute("UPDATE STAGECOACH SET time = time - 1")
        bot.cur.execute("DELETE FROM STAGECOACH WHERE time < 1")
        bot.cur.execute("SELECT * FROM STAGECOACH")
        heroes_after = len(bot.cur.fetchall())
        print("STAGECOACH | UPDATED {} | DELETED {} | TIME {}".format(heroes_before,
                                                                      heroes_before - heroes_after,
                                                                      (datetime.now() - now).microseconds / 10 ** 6))

    def check_stagecoach(self, player_info):
        self.bot.cur.execute("SELECT * FROM STAGECOACH WHERE playerID = {}".format(player_info["playerID"]))
        heroes = len(self.bot.cur.fetchall())
        while heroes < player_info["stagecoach_size"] + constants.STAGECOACH_BASE_SIZE:
            level = random.randint(0, player_info["stagecoach_level"])
            time = random.randint(1, constants.STAGECOACH_TIME_LIMIT)
            self.add_stagecoach(player_info["playerID"], level, time)
            heroes += 1
        return self.get_stagecoach(player_info["playerID"])

    def add_stagecoach(self, player_id, level, time):
        self.bot.cur.execute("SELECT * FROM ADVENTURER_LIST")
        adventurers = self.bot.cur.fetchall()
        new_adventurer = random.choice(adventurers)
        insert = [player_id, new_adventurer["advID"], level, time]
        self.bot.cur.execute("INSERT INTO STAGECOACH (playerID, advID, level, time) VALUES({}, {}, {}, {})".format(*insert))
        self.bot.con.commit()

    def get_stagecoach(self, player_id):
        self.bot.cur.execute("SELECT * FROM STAGECOACH WHERE playerID = {}".format(player_id))
        stagecoach = self.bot.cur.fetchall()
        return stagecoach
