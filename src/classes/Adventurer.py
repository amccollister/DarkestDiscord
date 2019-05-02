import src.constants as constants


class Adventurer(object):
    def __init__(self, bot, hero_id):
        self.bot = bot
        self.hero_id = hero_id
        self.adventurer = self.get_adventurer_info()
        self.stats = self.get_stats()

    def get_adventurer_info(self):
        return self.bot.db.get_row("ADVENTURERS", "heroID", self.hero_id)

    def get_stats(self):
        stats = {}
        base = self.bot.db.get_row("ADVENTURER_LIST", "advID", self.adventurer["advID"])
        for k, v in constants.LEVEL_UP:
            stats[k] = (v * self.adventurer["level"]) + base[k]
        return stats

    def add_exp(self):
        pass

    def level_up(self):
        pass