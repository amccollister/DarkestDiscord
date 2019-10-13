"""
Adventurer class for every character that a Player owns.
Instances should be persistent while the bot is active for every adventurer in play.
Instances will expire when the Adventurer does.

Variables:
???
    bot - the primary bot instance
    hero_id - id of the hero in the table
    player_id - id of the player that hired this hero
    info - a list of base stats from db
    stats - a list of proper stats post-modifiers for levelled hero
    trinkets - a list of up to two trinkets equipped by an Adventurer
    effects - a list of status effects afflicting an Adventurer
    quirks - a list of quirks afflicting an Adventurer
    skills - a list of up to four skills equipped by an Adventurer
Methods:
    get_adventurer_info


    Need methods for:
        trinkets
            get_trinkets
        effects
            get_effects
        quirks
            get_quirks
        skills
            get_skills
"""

import re
import src.constants as constants
import src.utils as util


class Adventurer(object):
    def __init__(self, bot, hero_id, player_id):
        #TODO: add equipped trinket information
        #TODO: reference quirks, effects, trinkets, skills, and maybe party?
        self.bot = bot
        self.hero_id = hero_id
        self.player_id = player_id
        self.info = self.get_adventurer_info()
        self.stats = self.get_stats()

    def get_adventurer_info(self):
        return self.bot.db.get_row("ADVENTURERS", "heroID", self.hero_id)

    def get_stats(self):
        base = self.bot.db.get_row("ADVENTURER_LIST", "advID", self.info["advID"])
        stats = {k: base[k] for k in base.keys()}
        for k, v in constants.LEVEL_UP.items():
            stats[k] += (v * self.info["level"])
        return stats

    def get_basic_info(self, index):
        emoji = constants.UNICODE_DIGITS[index]
        field_name = "{}\n{}".format(self.info["name"], self.get_class_level())
        field_value = "{}\nHP: {}\nStress: {}\nPress {} for stats".format(self.info["status"], self.get_hp(), self.get_stress(), emoji)
        return [field_name, field_value]

    def get_detailed_info(self):
        title = self.info["name"]
        description = self.get_class_level()
        author = self.bot.get_user(self.player_id)
        fields = self.get_embed_fields()
        embed = util.make_embed(title=title, description=description, fields=fields, author=author, thumbnail=author.avatar_url)
        return embed

    def get_hp(self):
        return "{}/{}".format(self.info["hp"], self.stats["max_hp"])

    def get_stress(self):
        return "{}/200".format(self.info["stress"])

    def get_class_level(self):
        return "Level {} {}".format(self.info["level"], self.stats["class"])

    def get_embed_fields(self):
        fields = self.stats.copy()
        output = [["DMG", "{}-{}".format(fields["dmg_lower"], fields["dmg_upper"])]]
        redundant = ["class", "advID", "max_hp", "dmg_lower", "dmg_upper"]
        res1 = ["stun_res", "blight_res", "disease_res", "death_blow_res"]
        res2 = ["move_res", "bleed_res", "debuff_res", "trap_res"]
        for k, v in fields.items():
            if k not in redundant + res1 + res2:
                output.append([k.upper(), v])
        output.append(["Resistances", "Stun: **{}%**\n"
                                      "Blight: **{}%**\n"
                                      "Disease: **{}%**\n"
                                      "Death Blow: **{}%**".format(*[fields[res] for res in res1])])
        output.append(["\U0000200b", "Move: **{}%**\n"
                                     "Bleed: **{}%**\n"
                                     "Debuff: **{}%**\n"
                                     "Trap: **{}%**".format(*[fields[res] for res in res2])])
        return output

    def add_exp(self):
        # also add a check if they're over the threshold. (calculate the threshold)
        pass

    def level_up(self):
        pass
