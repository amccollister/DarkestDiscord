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
        # self.stagecoach_refresh = self.bot.loop.create_task(self.refresh_stagecoach())

    async def refresh_stagecoach(self):
        await self.bot.wait_until_ready()
        while not self.bot.is_closed():
            # TODO: deduct one minute from all heroes in stagecoaches
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
        output = ""
        stagecoach = util.check_stagecoach(self.bot, ctx.author.id)
        react_heroes = {v:k for (k,v) in zip(stagecoach, constants.UNICODE_DIGITS)}
        for hero in stagecoach:
            name = util.get_adventurer(self.bot, hero["advID"])["name"]
            output += "Level {} {} | Leaving in {} minute(s)\n".format(hero["level"], name, hero["time"])
        msg = await util.send(ctx, output)
        for emote in constants.UNICODE_DIGITS[:len(stagecoach)]:
            await msg.add_reaction(emote)
        while True:
            try:
                # wait_for takes the parameters for the event. on_reaction_add has two parameters
                reaction, user = await self.bot.wait_for("reaction_add",
                                                         check=lambda r, u: u.id == ctx.author.id,
                                                         timeout=constants.STAGECOACH_REACT_TIME_LIMIT)
                if reaction.emoji in constants.UNICODE_DIGITS[:len(stagecoach)]:
                    hero = react_heroes[reaction.emoji]
                    name = util.get_adventurer(self.bot, hero["advID"])["name"]
                    await util.send(ctx, "You hired the Level {} {}!".format(hero["level"], name))
                    # TODO: remove hero from stagecoach and add hero to roster
            except asyncio.TimeoutError:
                break

    @commands.command()
    async def roster(self, ctx):
        await util.send(ctx, "This will display your roster")


def setup(bot):
    bot.add_cog(TownCog(bot))
