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
    def __init__(self, db, char_id):
        # TODO: grab effect information from the table
        self.db = db
        self.info = db.get_row("EFFECT", "charID", char_id)
        self.name = db.get_row("EFFECT_LIST", "effectID", self.info["effectID"])["name"]
        self.stat = self.info["stat"]
        self.modifier = self.info["modifier"]
        self.duration = self.info["duration"]

    def reduce_duration(self):
        self.duration -= 1

    def get_effect_info(self):
        self.info = self.db.get_row("EFFECT", "charID", self.info["char_id"])
