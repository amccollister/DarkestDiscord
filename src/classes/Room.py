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
    def __init__(self):
        pass

    def get_room_info(self):
        pass