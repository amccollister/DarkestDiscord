"""
This is the party class which will store a single party from the database per Discord guild.
Each party will contain four active adventurers ready to delve into a dungeon.

Variables:
    adventurers - a list of Adventurers in the party in appropriate order (0 1 2 3) with 3 being the front
    guild_id - the guild (and Dungeon) for the party
    info - a row from the Party table in the database

Methods:
    get_party_info - get a row from the party database based on discord guild id
    move_member - move a member forward or backward x spaces and shift the others
    add_member - insert a member into the party and database
    remove_member - delete a member from the party and database and shift remaining members
    make_leader - promote a single player to party leader
"""

class Party(object):
    def __init__(self, bot, party_id):
        #TODO: grab the party information from the table
        #TODO: reference the adventurers in the party and the dungeon they belong to
        self.party_id = party_id
        self.bot = bot
        self.info = self.get_party_info()
        # Important note: Darkest Dungeon party ranks read right to left. Enemy ranks are left to right.
        # Index 0 in arrangement is the first position. 0001
        # So in a battle, the first ranks of each team are as follows. 0001 1000
        self.arrangement = [self.info['pos1'], self.info['pos2'], self.info['pos3'], self.info['pos4']]
        self.leader = self.info["leaderID"]

    def get_party_info(self):
        return self.bot.db.get_row("PARTY", "partyID", self.party_id)

    def move_member(self, adv_id, pos):
        # Get the index of adv_id and increment by pos
        # Round it to the length of the array and find conflicts
        adv_pos = self.arrangement.index(adv_id)
        adv_pos = max(min(len(self.arrangement)-1, adv_pos+pos), 0) # Don't go above 4 or below 0.
        new_pos = adv_pos + pos
        if pos>0:
            # moving forward shifts folks backwards
            new_list = self.arrangement[:]
            for idx, _ in enumerate(new_list):
                if idx==new_pos:
                    new_list[idx] = self.arrangement[adv_id]
                elif idx<new_pos:
                    new_list[idx] = self.arrangement[idx-1]
                else:
                    new_list[idx] = self.arrangement[idx+1]
        else:
            # vice versa
            new_list = self.arrangement[:]
            for idx, _ in enumerate(new_list):
                if idx==new_pos:
                    new_list[idx] = self.arrangement[adv_id]
                elif idx<new_pos:
                    new_list[idx] = self.arrangement[idx+1]
                else:
                    new_list[idx] = self.arrangement[idx-1]

    def add_member(self, adv_id):
        # Use python index method
        for idx, val in enumerate(self.arrangement):
            if val == None:
                self.arrangement[idx] = adv_id
                break
        else:
            print("No space available in party")

    def remove_member(self, adv_id):
        # Use python index method
        for idx, val in enumerate(self.arrangement):
            if val == adv_id:
                self.arrangement[idx] = None

    def make_leader(self, player_id):
        # Transfer leadership to another player
        self.bot.db.update_row("PARTY", "leaderID={}".format(player_id), "partyID={}".format(self.party_id))