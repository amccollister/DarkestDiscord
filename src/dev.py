import src.utils as util
from discord.ext import commands

from datetime import datetime


class DevCog(commands.Cog):
    def __init__(self, bot):
        # grab bot attributes
        self.bot = bot

    async def cog_before_invoke(self, ctx):
        if ctx.author.id != 66357688275050496:
            raise commands.CommandError(message="You may not use developer commands")

    @commands.command()
    async def users(self, ctx):
        users = self.bot.users
        await util.send(ctx, "I can see {} people".format(len(users)))

    @commands.command()
    async def insert(self, ctx):
        now = datetime.now()
        self.bot.cur.execute("BEGIN TRANSACTION") # begin trans and commit is very important
        for u in self.bot.users:
            self.bot.cur.execute("INSERT OR IGNORE INTO PLAYERS VALUES({}, 0, 0, 0, 0, 0)".format(u.id))
        self.bot.cur.execute("COMMIT")
        self.bot.con.commit()
        passed = datetime.now() - now
        await util.send(ctx, "Added {} people in {} seconds".format(len(self.bot.users), passed.total_seconds()))



def setup(bot):
    bot.add_cog(DevCog(bot))
