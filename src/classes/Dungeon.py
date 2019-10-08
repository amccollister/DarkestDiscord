from src.classes.Party import Party
from src.constants import DEFAULT_PREFIX

"""
A dungeon is a single channel and party in a Discord guild.
Only dungeon commands may be performed within.

Task:   Handle the generation and storage of a single dungeon for a party to run.
        Respond to all the dungeon related commands within the dungeon channel.
        
"""
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
