import src.utils as util
from discord.ext import commands


class TownCog(commands.Cog):
    def __init__(self, bot):
        # grab bot attributes
        self.bot = bot


def setup(bot):
    bot.add_cog(TownCog(bot))
