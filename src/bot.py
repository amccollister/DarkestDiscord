import sys
import asyncio
from src import utils

import sqlite3 as sql
import src.constants as constants
from discord.ext.commands import Bot

# TODO: set a background task to sync Channel table with all connected servers each minute

class DarkestBot(Bot):
    def __init__(self):
        super().__init__(constants.DEFAULT_PREFIX)
        self.remove_command('help')  # We will be implementing our own.

        # establish sql connection here
        self.con = sql.connect("db/database.db", isolation_level=None)
        self.cur = self.con.cursor()
        with open('db/schema.sql') as schema:
            self.cur.executescript(schema.read())

        #start background tasks (https://github.com/Rapptz/discord.py/blob/master/examples/background_task.py)
        self.sync = self.loop.create_task(self.sync_servers())

    def run(self):
        super().run(constants.BOT_TOKEN)

    def get_prefix(self, message):
        #TODO: dynamic prefix thing
        #https://discordpy.readthedocs.io/en/rewrite/ext/commands/api.html#bot
        pass

    async def on_ready(self):
        print("------------")
        print("Logged in as")
        print(self.user.name)
        print(self.user.id)
        print("------------")
        self.load_extension("src.setup")
        #for plugin in constants.PLUGINS:
        #    self.load_extension("src.{}".format(plugin))

    #TODO: dynamic prefix using command_prefix
    async def on_message(self, message):
        if message.author.id != self.user.id:
            print("{0.author}: {0.content}".format(message))
        await self.process_commands(message)

    async def on_error(self, event, *args, **kwargs):
        print(sys.exc_info())
        print("ERROR: {}".format(event))

    async def on_command_error(self, ctx, e):
        ctx.command = "ERROR"
        await utils.send(ctx, e)

    # synchronize all connected servers
    async def sync_servers(self):
        await self.wait_until_ready()
        while not self.is_closed():
            self.cur.execute("SELECT * FROM CHANNEL")
            db_guilds = self.cur.fetchall()
            bot_guilds = [x.id for x in self.guilds]
            for guild in bot_guilds:
                if guild not in db_guilds:
                    self.cur.execute("INSERT OR IGNORE INTO CHANNEL VALUES({id}, NULL, NULL, '{pre}')"
                                     .format(id=guild, pre=constants.DEFAULT_PREFIX))
                    self.con.commit()
            print(db_guilds)
            await asyncio.sleep(60)
