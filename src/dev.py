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
    async def get(self, ctx):
        self.bot.cur.execute("SELECT * FROM PLAYERS")
        p = self.bot.cur.fetchone()
        out = ["{} {}".format(x, p[x]) for x in p.keys()]
        output = "\n".join(out)
        await util.send(ctx, output)


def setup(bot):
    bot.add_cog(DevCog(bot))
