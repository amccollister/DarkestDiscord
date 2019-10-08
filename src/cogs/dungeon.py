import src.utils as util
from discord.ext import commands


class DungeonCog(commands.Cog):
    def __init__(self, bot):
        # grab bot attributes
        self.bot = bot

    async def cog_before_invoke(self, ctx):
        if not ctx.guild:
            raise commands.CommandError(message="You may not use dungeon commands through direct message.")
        dungeon = self.bot.get_dungeon(ctx.guild.id)
        channel = self.bot.get_channel(dungeon.info["dungeon_channel"])
        if not channel:
            raise commands.CommandError(message="You may not use dungeon commands until the channel has been set.")
        elif channel.id != ctx.channel.id:
            raise commands.CommandError(message="You may not use dungeon commands outside of {}.".format(channel.mention))

    @commands.command()
    async def attack(self, ctx):
        await util.send(ctx, "You attacked!")


def setup(bot):
    bot.add_cog(DungeonCog(bot))
