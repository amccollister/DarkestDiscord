"""
This is the party class which will store a single party from the database per Discord guild.
Each party will contain four active adventurers ready to delve into a dungeon.

Variables:
    adventurers - a list of Adventurers in the party
    guild_id - the guild (and Dungeon) for the party
    info - a row from the Party table in the database

Methods:
    get_party_info - get a row from the party database based on discord guild id
    move_member - move a member forward or backward x spaces and shift the others
    
"""

class Party(object):
    def __init__(self, bot, party_id):
        #TODO: grab the party information from the table
        #TODO: reference the adventurers in the party and the dungeon they belong to
        # learn about locals and globals for the purposes of existing adventurer classes
        self.info = self.get_party_info()
        pass

    def get_party_info(self):
        pass