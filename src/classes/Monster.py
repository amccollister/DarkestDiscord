"""
Monster class for storing enemies in the game.
One instance created for each monster in any dungeon.
Stats are nearly identical to Adventurer's aside from crit bonus.

Variables:
    monster_id
    info - list of columns from the table
    effects - a list of status effects afflicting a Monster
    skills - a list of up to four skills equipped by a Monster
Methods:
    get_monster_info

    Need methods for
        skills (Skills are immutable and set per monster. Shouldn't have add or remove)
            get_skills
            use_skill - pick a random? skill and target
        effects
            get_effects
            add_effect
            remove_effect

"""

class Monster(object):
    def __init__(self):
        #TODO: grab the monster stats and information from the table
        pass