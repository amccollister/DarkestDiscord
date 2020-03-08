"""
Player class for each user known by the bot.
It is the cornerstone for all updates regarding the player's heroes, inventory, roster, and stagecoach.

Variables:
    bot - primary bot instance
    player_id - Player's ID
    info - a list of the Player's info in the db
    roster - a list of the Adventurers in the Player's roster
    stagecoach - an instance of a Stagecoach for the Player
    inventory - a dictionary of itemIDs mapped to number of items in a Player's inventory
Methods:
    update_info
    get_player_info
    get_roster
    get_roster_cap
    get_adventurer
    level_up
    add_resource
    hire
    fire
    get_building_cost
    get_building_cost_string
    check_afford_building_cost
"""

import src.constants as constants
from src.classes.Stagecoach import Stagecoach
from src.classes.Adventurer import Adventurer


class Player(object):
    def __init__(self, bot, player_id):
        #TODO: add inventory information
        self.bot = bot
        self.player_id = player_id
        self.info = self.get_player_info()
        self.roster = self.get_roster()
        self.stagecoach = Stagecoach(bot, self)

    def update_info(self):
        self.__init__(self.bot, self.player_id)

    def get_player_info(self):
        self.bot.db.insert_row("PLAYERS", ["playerID"], [self.player_id])
        return self.bot.db.get_row("PLAYERS", "playerID", self.player_id)

    def get_roster(self):
        heroes = self.bot.db.get_rows("ADVENTURERS", "playerID", self.player_id)
        return [Adventurer(self.bot, hero["heroID"]) for hero in heroes]

    def get_roster_cap(self):
        return constants.ADVENTURER_BASE_CAPACITY + self.info["roster_size_level"]

    def get_adventurer(self):
        pass

    def level_up(self, column):
        if self.info[column] >= constants.UPGRADE_MAX_LEVEL:
            return False
        self.bot.db.update_row("PLAYERS", "{0} = {0} + 1".format(column), "playerID = {}"
                               .format(self.player_id))
        self.update_info()
        return True

    def add_resource(self, column, amount):
        self.bot.db.update_row("PLAYERS", "{0} = {0} + {1}".format(column, amount), "playerID = {}"
                               .format(self.player_id))
        self.update_info()
        return "Increased {} by {}".format(column, amount)

    def hire(self, stagecoach_hire):
        if len(self.bot.db.get_rows("ADVENTURERS", "playerID", self.player_id)) >= self.get_roster_cap():
            return False
        stagecoach_id = stagecoach_hire["stagecoachID"]
        adv_id = stagecoach_hire["advID"]
        self.bot.db.delete_rows("STAGECOACH", "stagecoachID = {}".format(stagecoach_id))
        adv_class = self.stagecoach.get_class_row(adv_id)
        hp = adv_class["max_hp"] + stagecoach_hire["level"] * constants.LEVEL_UP["max_hp"]
        columns = ["advID", "playerID", "level", "hp", "name"]
        values = [adv_id, self.player_id, stagecoach_hire["level"], hp, stagecoach_hire["name"]]
        self.bot.db.insert_row("ADVENTURERS", columns, values)
        self.roster = self.get_roster()
        return True

    def fire(self, fired_hero):
        if not fired_hero.get_adventurer_info():
            return False
        self.bot.db.delete_rows("ADVENTURERS", "heroID = {}".format(fired_hero.info["heroID"]))
        self.update_info()
        return True

    def get_building_cost(self, name):
        price = {}
        level = self.info[name]
        base_cost = self.bot.db.get_row("TOWN_BASE_COST", "name", name)
        level_cost = self.bot.db.get_row("TOWN_UPGRADE_COST", "name", name)
        for key in base_cost.keys():
            if key != "name":
                price[key] = base_cost[key] + (level * level_cost[key])
        return price

    def get_building_cost_string(self, name):
        output = ""
        cost = self.get_building_cost(name)
        for key, value in cost.items():
            if int(value) > 0:
                output += "{}: {}\n".format(key.capitalize(), value)
        return output

    def check_afford_building_cost(self, name):
        cost = self.get_building_cost(name)
        for key, value in cost.items():
            if int(value) > self.info[key]:
                return False
        return True