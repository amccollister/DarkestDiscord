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
        self.stagecoach_refresh = self.bot.loop.create_task(self.refresh_stagecoach())

    async def refresh_stagecoach(self):
        await self.bot.wait_until_ready()
        while not self.bot.is_closed():
            now = datetime.now()
            self.bot.cur.execute("SELECT * FROM STAGECOACH")
            heroes_before = len(self.bot.cur.fetchall())
            self.bot.cur.execute("UPDATE STAGECOACH SET time = time - 1")
            self.bot.cur.execute("DELETE FROM STAGECOACH where time < 1")
            self.bot.cur.execute("SELECT * FROM STAGECOACH")
            heroes_after = len(self.bot.cur.fetchall())
            print("STAGECOACH | UPDATED {} | DELETED {} | TIME {}".format(heroes_before,
                                                                          heroes_before-heroes_after,
                                                                          (datetime.now() - now).microseconds/10**6))
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
        react_heroes = {v: k for (k, v) in zip(stagecoach, constants.UNICODE_DIGITS)}
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
                    hired = util.hire_adventurer(self.bot, ctx.author.id, react_heroes[reaction.emoji])
                    await util.send(ctx, hired)
            except asyncio.TimeoutError:
                break

    @commands.command()
    async def roster(self, ctx):
        output = ""
        heroes = util.get_roster(self.bot, ctx.author.id)
        if not heroes:
            output = "You have no heroes in your roster."
        else:
            for hero in heroes:
                output += "Level {} {} | Status: {}\n".format(hero["level"], hero["character_name"], hero["status"])
        await util.send(ctx, output)


def setup(bot):
    bot.add_cog(TownCog(bot))
