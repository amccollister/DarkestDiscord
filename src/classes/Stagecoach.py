import random
import src.constants as constants

from datetime import datetime
# TODO: Code this better I think


class Stagecoach(object):
    def __init__(self, bot, player):
        self.bot = bot
        self.player = player
        self.adv_list = self.check_stagecoach()

    @staticmethod
    def refresh_stagecoach(bot):
        now = datetime.now()
        heroes_before = bot.db.get_row_count("STAGECOACH")
        bot.db.update_rows("STAGECOACH", "time = time - 1")
        bot.db.delete_rows("STAGECOACH", "time < 1")
        heroes_after = bot.db.get_row_count("STAGECOACH")
        print("STAGECOACH | UPDATED {} | DELETED {} | TIME {}".format(heroes_before,
                                                                      heroes_before - heroes_after,
                                                                      (datetime.now() - now).microseconds / 10 ** 6))

    def check_stagecoach(self):
        hero_count = len(self.bot.db.get_rows("STAGECOACH", "playerID", self.player.player_id))
        hero_cap = self.player.info["stagecoach_size"] + constants.STAGECOACH_BASE_SIZE
        while hero_count < hero_cap:
            level = random.randint(0, self.player.info["stagecoach_level"])
            time = random.randint(1, constants.STAGECOACH_TIME_LIMIT)
            self.add_stagecoach(level, time)
            hero_count += 1
        return self.bot.db.get_rows("STAGECOACH", "playerID", self.player.player_id)

    def add_stagecoach(self, level, time):
        adventurer_count = self.bot.db.get_row_count("ADVENTURER_LIST")
        new_adventurer = random.randint(1, adventurer_count-1)
        columns = ["playerID", "advID", "level", "time"]
        values = [self.player.info["playerID"], new_adventurer, level, time]
        self.bot.db.insert_row("STAGECOACH", columns, values)

    def get_class(self, adv_id):
        return self.bot.db.get_row("ADVENTURER_LIST", "advID", adv_id)

    def get_class_name(self, adv_id):
        return self.bot.db.get_row("ADVENTURER_LIST", "advID", adv_id)["name"]

    def hire(self, stagecoach_hire):
        stagecoach_id = stagecoach_hire["stagecoachID"]
        adv_id = stagecoach_hire["advID"]
        if len(self.bot.db.get_rows("ADVENTURERS", "playerID", self.player.player_id)) >= self.player.get_roster_cap():
            return False
        self.bot.db.delete_rows("STAGECOACH", "stagecoachID = {}".format(stagecoach_id))
        adv_class = self.get_class(adv_id)
        hp = adv_class["max_hp"] + stagecoach_hire["level"]*constants.LEVEL_UP["max_hp"]
        columns = ["advID", "playerID", "level", "hp", "character_name"]
        values = [adv_id, self.player.player_id, stagecoach_hire["level"], hp, adv_class["name"]]
        self.bot.db.insert_row("ADVENTURERS", columns, values)
        return True
