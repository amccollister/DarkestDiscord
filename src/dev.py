import src.utils as util
from discord.ext import commands


class DevCog(commands.Cog):
    def __init__(self, bot):
        # grab bot attributes
        self.bot = bot

    async def cog_before_invoke(self, ctx):
        if ctx.author.id != 66357688275050496:
            raise commands.CommandError(message="You may not use developer commands")

    @commands.command()
    async def dev(self, ctx):
        self.bot.cur.execute("SELECT * FROM ITEM_LIST")
        output = self.bot.cur.fetchall()
        await util.send(ctx, output)


def setup(bot):
    bot.add_cog(DevCog(bot))
