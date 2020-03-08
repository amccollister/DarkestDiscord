"""
Item class for every owned item by players.
Instance will expire when the item is no longer owned.

Variables:
    player_id
    item_id
    item_type
    value
    type - value indicating if it is consumable
Methods:
    get_item_info
"""


class Item(object):
    def __init__(self, db, item_id):
        # TODO: Will need effects and such
        self.item_id = item_id
        self.db = db
        self.info = self.get_item_info()
        self.value = self.info["cost"]
        self.type = self.info["type"]

    def get_item_info(self):
        return self.db.get_row("ITEM_LIST", "itemID", self.item_id)