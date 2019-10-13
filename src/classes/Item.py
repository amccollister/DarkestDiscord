"""
Item class for every owned item by players.
Instance will expire when the item is no longer owned.

Variables:
    player_id
    item_id
    item_type
    value
    consumable - boolean value indicating if it can be used
Methods:
    get_item_info

"""


class Item(object):
    def __init__(self, bot, item_id):
        # TODO: Get id, item type, and gold costs as well as item uses
        pass

    def get_item_info(self):
        pass