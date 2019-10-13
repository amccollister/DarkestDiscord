"""
Skill class for each skill known by an adventurer.
Each user's skill will have different effects, so we need one for each player.
Instance will expire when an Adventurer removes it from their skill list.

Variables:
    skill_id - the id of the skill in the database
    hero_id - the id of the Adventurer with this skill equipped.
    level - the level of this skill
    lower - the lower bound this skill can roll
    upper - the upper bound this skill can roll
    range - denotes melee or ranged
    rank - 4 digit binary number incidating positions skill can be used from
    target - 8 digit binary number indicating the positions the skill can target
    acc_mod - the accuracy modifier for this skill
    crit_mod - the crit modifier for this skill
Methods:
    get_skill_info - grab the skill row from the table
    generate_effect - generate the numbers rolled for the skill
"""


class Skill(object):
    def __init__(self):
        # TODO: get the skill information and modifiers
        pass

    def get_skill_info(self):
        pass

    def generate_effect(self):
        pass
