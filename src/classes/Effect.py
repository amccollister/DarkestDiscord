"""
Effect stores any active buffs or debuffs on an Adventurer or Monster
They are time based by turns and wear off over time.

Variables:
    effect_id - the id of the effect in the database
    name
    stat
    modifier
    duration
Methods:
    get_effect_info
    reduce_duration
"""

class Effect(object):
    def __init__(self):
        # TODO: grab effect information from the table
        pass