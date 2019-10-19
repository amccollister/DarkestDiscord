"""
Dungeon class for each registered guild.
Contains all the dungeon, monster, encounter, and loot information for each room.
This also contains and sets the prefix for each guild.
Instance expires when a guild is no longer registered.

Variables:
    bot
    guild_id
    info
    party - the Party delving this dungeon
    rooms - a list of all Rooms in the dungeon
    mission - the mission statement for the party
    reward - a list of items awarded upon mission completion
    location - the room that the party currently occupies
Methods:
    update_info
    get_dungeon_info
    generate_dungeon - generates the Rooms, mission, and rewards for the dungeon
    generate_map - create a map for the whole dungeon including the player location
    set_party
    set_channel
    set_prefix
    move_party
    start_mission
    complete_mission

"""

from src.classes.Party import Party
from src.constants import DEFAULT_PREFIX


class Dungeon(object):
    def __init__(self, bot, guild_id):
        self.bot = bot
        self.guild_id = guild_id
        self.info = self.get_dungeon_info()
        self.party = None
        if not self.info["prefix"]:
            self.set_prefix(DEFAULT_PREFIX)

    def update_info(self):
        self.info = self.get_dungeon_info()

    def get_dungeon_info(self):
        self.bot.db.insert_row("DUNGEON", ["guildID"], [self.guild_id])
        return self.bot.db.get_row("DUNGEON", "guildID", self.guild_id)

    def set_channel(self, channel_type, channel_id):
        column = channel_type + "_channel"
        self.bot.db.update_row("DUNGEON", "{0} = {1}".format(column, channel_id), "guildID = {}".format(self.guild_id))
        self.update_info()

    def set_prefix(self, prefix_name):
        self.bot.db.update_row("DUNGEON", "prefix = \"{0}\"".format(prefix_name), "guildID = {}".format(self.guild_id))
        self.update_info()

    def set_party(self, party_id, party : Party):
        self.party = party
        self.bot.db.update_row("DUNGEON", "partyID = {0}".format(party_id), "guildID = {}".format(self.guild_id))
        self.update_info()
