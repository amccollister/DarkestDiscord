"""
Skill class for each skill known by an adventurer.
Each user's skill will have different effects, so we need one for each player.
Instance will expire when an Adventurer removes it from their skill list.

Variables:
    skill_id - the id of the skill in the database
    hero_id - the id of the Adventurer with this skill equipped.
    level - the level of this skill
Methods:
    get_skill_info - grab the skill row from the table
    generate_effect - generate the numbers rolled for the skill
"""


class Skill(object):
    def __init__(self):
        # TODO: get the skill information and modifiers
        pass