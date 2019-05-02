import sys
import asyncio
import src.utils as util
import sqlite3 as sql
import src.constants as constants

from discord.ext.commands import Bot
from src.classes.Player import Player
from src.classes.SQLHandler import SQLHandler
from datetime import datetime

# TODO: make classes
class DarkestBot(Bot):
    def __init__(self):
        # initialize bot
        super().__init__(command_prefix=util.get_pre)
        self.remove_command('help')  # We will be implementing our own.

        # establish sql connection here
        self.db = SQLHandler()
        #self.con = sql.connect("db/database.db", isolation_level=None)
        #self.con.row_factory = sql.Row
        #self.cur = self.con.cursor()
        #with open('db/schema.sql') as schema:
        #    self.cur.executescript(schema.read())

        # start background tasks (https://github.com/Rapptz/discord.py/blob/master/examples/background_task.py)
        # might not be needed?

    def run(self):
        super().run(constants.BOT_TOKEN)

    def sync_servers(self):
        bot_guilds = [x.id for x in self.guilds]
        for gid in bot_guilds:
            columns = ["guildID", "prefix"]
            values = [gid, constants.DEFAULT_PREFIX]
            self.db.insert_row("CHANNEL", columns, values)


    async def on_ready(self):
        self.sync_servers()
        print("------------")
        print("Logged in as")
        print(self.user.name)
        print(self.user.id)
        print("------------")

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
