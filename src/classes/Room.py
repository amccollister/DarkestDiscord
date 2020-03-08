"""
Room class for every room in a dungeon.
Class will expire when a dungeon is cleared.

Variables:
    room_id - the id of the room in the database
    monsters - a list of Monsters in the Room
    treasure - a list of Items in in the Room
    previous - the Room before this one
    next - the Room after this one
    encounter - ?

Methods:
    get_room_info - grab the row from the database
    generate_room - get the monsters/loot/encounters in a room.
"""

class Room(object):
    def __init__(self, bot, room_id):
        self.bot = bot
        self.room_id = room_id
        self.info = self.get_room_info()
        self.monsters = None
        self.treasure = None
        self.previous = None
        self.next = None
        self.encounter = None

    def get_room_info(self):
        return self.bot.db.get_row("ROOM", "roomID", self.room_id)

    def generate_room(self):
        # Randomly seed a room using some algorithm
        pass