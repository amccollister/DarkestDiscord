import sys
import src.utils as util
import src.constants as constants

from discord.ext.commands import AutoShardedBot
from src.classes.SQLHandler import SQLHandler
from src.classes.Dungeon import Dungeon
from src.classes.Player import Player


class DarkestBot(AutoShardedBot):
    def __init__(self):
        # initialize bot
        super().__init__(command_prefix=self.get_pre)
        self.remove_command('help')  # We will be implementing our own.

        # object lists for all the guilds and players
        self.dungeons = {}
        self.players = {}

        # establish sql connection here
        self.db = SQLHandler()

        # start background tasks (https://github.com/Rapptz/discord.py/blob/master/examples/background_task.py)
        # might not be needed?
        # TODO: db backup

    def run(self):
        super().run(constants.BOT_TOKEN)

    def get_pre(self, _, ctx):
        if not ctx.guild:
            return constants.DEFAULT_PREFIX
        dungeon = self.get_dungeon(ctx.guild.id)
        return dungeon.info["prefix"]

    def sync_servers(self):
        bot_guilds = [x.id for x in self.guilds]
        for gid in bot_guilds:
            self.dungeons[gid] = Dungeon(self, gid)

    def get_dungeon(self, guild_id):
        if guild_id not in self.dungeons:
            self.dungeons[guild_id] = Dungeon(self, guild_id)
        return self.dungeons[guild_id]

    def get_player(self, player_id):
        if player_id not in self.players:
            self.players[player_id] = Player(self, player_id)
        return self.players[player_id]

    async def on_ready(self):
        print("------------")
        print("Logged in as")
        print(self.user.name)
        print(self.user.id)
        print("------------")
        constants.BOT_AVATAR = self.user.avatar_url  # set the avatar for embeds
        self.sync_servers()

    async def on_guild_join(self):
        #TODO: add the server and dm the owner
        pass

    async def on_message(self, message):
        if message.author.id != self.user.id:
            print("{0.author}: {0.content}".format(message))
        await self.process_commands(message)

    async def on_error(self, event, *args, **kwargs):
        print(sys.exc_info())
        print("ERROR: {}".format(event))

    # TODO: test this when the bot can't message that channel
    async def on_command_error(self, ctx, e):
        ctx.command = "ERROR"
        await util.send(ctx, e)
