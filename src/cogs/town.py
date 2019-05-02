import random
import asyncio
import src.utils as util
import src.constants as constants

from datetime import datetime
from discord.ext import commands
from src.classes.Player import Player
from src.classes.Stagecoach import Stagecoach


class TownCog(commands.Cog):
    def __init__(self, bot):
        # grab bot attributes
        self.bot = bot

        # Town Background Tasks
        self.stagecoach_refresh = self.bot.loop.create_task(self.refresh_stagecoach())

    async def refresh_stagecoach(self):
        await self.bot.wait_until_ready()
        while not self.bot.is_closed():
            Stagecoach.refresh_stagecoach(self.bot)
            await asyncio.sleep(60)

    async def cog_before_invoke(self, ctx):
        channel = util.get_db_channel(ctx.bot, "town", ctx.guild.id)
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
        player = Player(ctx.bot, ctx.author.id)
        stagecoach = player.stagecoach.adventurers
        react = {v: k for (k, v) in zip(stagecoach, constants.UNICODE_DIGITS)}
        for adv in stagecoach:
            name = ctx.bot.db.get_row("ADVENTURER_LIST", "advID", adv["advID"])["name"]
            output += "Level {} {} | Leaving in {} minute(s)\n".format(adv["level"], name, adv["time"])
        msg = await util.send(ctx, output)
        for emote in constants.UNICODE_DIGITS[:len(stagecoach)]:
            await msg.add_reaction(emote)
        while True:
            try:
                # wait_for takes the parameters for the event. on_reaction_add has two parameters
                reaction, user = await ctx.bot.wait_for("reaction_add",
                                                         check=lambda r, u: u.id == ctx.author.id,
                                                         timeout=constants.STAGECOACH_REACT_TIME_LIMIT)
                if reaction.emoji in constants.UNICODE_DIGITS[:len(stagecoach)]:
                    hired = player.hire_adventurer(react[reaction.emoji])
                    await util.send(ctx, hired)
            except asyncio.TimeoutError:
                break

    @commands.command()
    async def roster(self, ctx):
        output = ""
        heroes = ctx.bot.db.get_rows("ADVENTURERS", "playerID", ctx.author.id)
        if not heroes:
            output = "You have no heroes in your roster."
        else:
            for hero in heroes:
                output += "Level {} {} | Status: {}\n".format(hero["level"], hero["character_name"], hero["status"])
        await util.send(ctx, output)


def setup(bot):
    bot.add_cog(TownCog(bot))
