"""
Quirk class holds information for permanent adventurer buffs.
Each instance of a quirk must be held by an adventurer who can have many quirks.
Should contain a column and mod to be used by the Adventurer class. i.e. (spd, -2) for -2 SPD

Variables:
    quirk_id - the id of the Quirk
    name - the name of th Quirk
    stat - the stat affected by the Quirk
    modifier - the mod of the Quirk
Methods:
    get_quirk_info
"""

class Quirk(object):
    def __init__(self):
        #TODO: grab quirk information from the table
        pass