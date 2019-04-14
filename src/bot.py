import sys

import sqlite3 as sql
import src.constants as constants
from discord.ext.commands import Bot


class DarkestBot(Bot):
    def __init__(self):
        super().__init__(constants.DEFAULT_PREFIX)
        self.remove_command('help')  # We will be implementing our own.
        #establish sql connection here
        self.con = sql.connect("db/database.db", isolation_level=None)
        self.cur = self.con.cursor()

    def run(self):
        super().run(constants.BOT_TOKEN)

    async def on_ready(self):
        print("------------")
        print("Logged in as")
        print(self.user.name)
        print(self.user.id)
        print("------------")
        self.load_extension("src.setup")
        #for plugin in constants.PLUGINS:
        #    self.load_extension("src.{}".format(plugin))

    async def on_message(self, message):
        if message.author.id != self.user.id:
            print("{0.author}: {0.content}".format(message))
        await self.process_commands(message)

    async def on_error(self, event, *args, **kwargs):
        print(sys.exc_info())
        print("ERROR: {}".format(event))
