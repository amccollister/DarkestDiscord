import src.constants as constants


class Adventurer(object):
    def __init__(self, bot, hero_id):
        self.bot = bot
        self.hero_id = hero_id
        self.info = self.get_adventurer_info()
        self.stats = self.get_stats()

    def get_adventurer_info(self):
        return self.bot.db.get_row("ADVENTURERS", "heroID", self.hero_id)

    def get_stats(self):
        base = self.bot.db.get_row("ADVENTURER_LIST", "advID", self.info["advID"])
        stats = {k: base[k] for k in base.keys()}
        for k, v in constants.LEVEL_UP.items():
            stats[k] = (v * self.info["level"]) + base[k]
        return stats

    def get_basic_info(self, index):
        emoji = constants.UNICODE_DIGITS[index]
        field_name = "{}\nLevel {} {}".format(self.info["name"], self.info["level"], self.stats["class"])
        field_value = "{}\nHP: {}/{}\nStress: {}/200\nPress {} for stats".format(self.info["status"], self.info["hp"], self.stats["max_hp"], self.info["stress"], emoji)
        return [field_name, field_value]


    def add_exp(self):
        pass

    def level_up(self):
        pass