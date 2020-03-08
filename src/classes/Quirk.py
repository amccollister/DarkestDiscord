"""
Quirk class holds information for permanent adventurer buffs.
Each instance of a quirk must be held by an adventurer who can have many quirks.
Should contain a column and mod to be used by the Adventurer class. i.e. (spd, -2) for -2 SPD

Variables:
    quirk_id - the id of the Quirk
    name - the name of the Quirk
    stat - the stat affected by the Quirk
    modifier - the mod of the Quirk
    positive - boolean value noting positive or negative quirk
Methods:
    get_quirk_info - grab info from table based on the id of the quirk
    get_modifier - obtain the modifier of the quirk and submit to the database
"""

class Quirk(object):
    def __init__(self, bot, quirk_id):
        #TODO: grab quirk information from the table
        self.bot = bot
        self.quirk_id = quirk_id
        self.info = self.get_quirk_info()

    def get_quirk_info(self):
        return self.bot.db.get_row("QUIRK_LIST", "quirkID", self.quirk_id)

    def get_modifier(self):
        pass