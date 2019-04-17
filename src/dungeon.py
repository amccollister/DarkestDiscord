import src.utils as util
from discord.ext import commands


class DungeonCog(commands.Cog):
    def __init__(self, bot):
        # grab bot attributes
        self.bot = bot


def setup(bot):
    bot.add_cog(DungeonCog(bot))
