import src.utils as util
from discord.ext import commands


class DungeonCog(commands.Cog):
    def __init__(self, bot):
        # grab bot attributes
        self.bot = bot

    async def cog_before_invoke(self, ctx):
        channel = util.get_db_channel(self.bot, "dungeon", ctx.guild.id)
        if channel.id != ctx.channel.id:
            raise commands.CommandError(message="You may not use dungeon commands outside of {}.".format(channel.mention))

    @commands.command()
    async def attack(self, ctx):
        await util.send(ctx, "You attacked!")

def setup(bot):
    bot.add_cog(DungeonCog(bot))
