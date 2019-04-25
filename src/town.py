import random
import asyncio
import src.utils as util
import src.constants as constants
from datetime import datetime

from discord.ext import commands


class TownCog(commands.Cog):
    def __init__(self, bot):
        # grab bot attributes
        self.bot = bot

        # Town Background Tasks
        # TODO: random timed adventurers in stagecoach unique to each player
        # self.stagecoach_refresh = self.bot.loop.create_task(self.refresh_stagecoach())

    async def refresh_stagecoach(self):
        await self.bot.wait_until_ready()
        while not self.bot.is_closed():
            print("Updated x chars in the stagecoach in x seconds")
            await asyncio.sleep(60)

    async def cog_before_invoke(self, ctx):
        channel = util.get_db_channel(self.bot, "town", ctx.guild.id)
        if not channel:
            raise commands.CommandError(message="You may not use town commands until the channel has been set.")
        elif channel.id != ctx.channel.id:
            raise commands.CommandError(message="You may not use town commands outside of {}.".format(channel.mention))

    @commands.command()
    async def shop(self, ctx):
        await util.send(ctx, "You entered the shop!")

    @commands.command()
    async def stagecoach(self, ctx):
        pass
        # run the check stagecoach util. update with level cap and hero cap. then display. Sort by time
        # use a dict


        #msg = await util.send(ctx, output)
        #for emote in constants.UNICODE_DIGITS[:total]:
        #    await msg.add_reaction(emote)

    @commands.command()
    async def roster(self, ctx):
        await util.send(ctx, "This will display your roster")


def setup(bot):
    bot.add_cog(TownCog(bot))
