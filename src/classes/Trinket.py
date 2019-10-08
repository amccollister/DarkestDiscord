"""
Trinket class for every equipped trinket by an adventurer.
When unequipped, should return to the user's inventory and become an Item.

Variables:

Methods:

"""

from src.classes.Item import Item


class Trinket(Item):
    def __init__(self, bot, item_id):
        super().__init__(bot, item_id)
        # TODO: Get rarity and additional effects as well and equip it?
        pass

    def get_trinket_info(self):
        pass