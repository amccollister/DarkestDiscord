import sys
import asyncio
import src.utils as util
import sqlite3 as sql
import src.constants as constants

from discord.ext.commands import Bot
from datetime import datetime

# TODO: make classes
class DarkestBot(Bot):
    def __init__(self):
        # initialize bot
        super().__init__(command_prefix=util.get_pre)
        self.remove_command('help')  # We will be implementing our own.

        # establish sql connection here
        self.con = sql.connect("db/database.db", isolation_level=None)
        self.con.row_factory = sql.Row
        self.cur = self.con.cursor()
        with open('db/schema.sql') as schema:
            self.cur.executescript(schema.read())

        # start background tasks (https://github.com/Rapptz/discord.py/blob/master/examples/background_task.py)
        # might not be needed?
        self.server_sync = self.loop.create_task(self.sync_servers())
        self.player_sync = self.loop.create_task(self.sync_players())

    def run(self):
        super().run(constants.BOT_TOKEN)

    async def on_ready(self):
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
            await asyncio.sleep(60)

    # synchronize all connected players
    async def sync_players(self):
        await self.wait_until_ready()
        while not self.is_closed():
            now = datetime.now()
            id_list = [u.id for u in self.users]
            util.add_players(self, id_list)
            time = datetime.now() - now
            print("SYNC PLAYERS | USERS {} | TIME {}".format(len(self.users), time.microseconds/10**6))
            await asyncio.sleep(60)
