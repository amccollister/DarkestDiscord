import src.constants as constants

class Adventurer(object):
    def __init__(self, bot, hero_id):
        self.bot = bot
        self.hero_id = hero_id
        self.adventurer = self.get_adventurer_info()
        self.stats = self.get_stats()

    def get_adventurer_info(self):
        self.bot.cur.execute("SELECT * FROM ADVENTURERS WHERE heroID = {}".format(self.hero_id))
        hero = self.bot.cur.fetchone()
        return hero

    def get_stats(self):
        stats = {}
        self.bot.cur.execute("SELECT * FROM ADVENTURER_LIST where advID = {}".format(self.adventurer["advID"]))
        base = self.bot.cur.fetchone()
        for k, v in constants.LEVEL_UP:
            stats[k] = (v * self.adventurer["level"]) + base[k]
        return stats



    def add_exp(self):
        pass

    def level_up(self):
        pass