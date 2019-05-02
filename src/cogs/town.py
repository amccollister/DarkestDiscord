import asyncio
import src.utils as util
import src.constants as constants

from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType
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
        #TODO: let commands work in DMs
        channel = util.get_db_channel(ctx.bot, "town", ctx.guild.id)
        if not channel:
            raise commands.CommandError(message="You may not use town commands until the channel has been set.")
        elif channel.id != ctx.channel.id:
            raise commands.CommandError(message="You may not use town commands outside of {}.".format(channel.mention))

    @commands.command()
    async def shop(self, ctx):
        await util.send(ctx, "You entered the shop!")

    @commands.command()
    @commands.cooldown(1, constants.STAGECOACH_COOLDOWN, BucketType.user)
    async def stagecoach(self, ctx):
        player = Player(ctx.bot, ctx.author.id)
        adv_list = player.stagecoach.adv_list
        react = {v: k for (k, v) in zip(adv_list, constants.UNICODE_DIGITS)}
        output = ["Level {} {} | Leaving in {} minute(s)".format
                  (adv["level"], player.stagecoach.get_class(adv["advID"]), adv["time"]) for adv in adv_list]
        msg = await util.react_send(ctx, "\n".join(output), constants.UNICODE_DIGITS[:len(adv_list)])
        while True:
            try:
                reaction, user = await ctx.bot.wait_for("reaction_add",
                                                        check=lambda r, u: u.id == ctx.author.id,
                                                        timeout=constants.STAGECOACH_REACT_TIME_LIMIT)
                if reaction.emoji in react.keys():
                    adv = react[reaction.emoji]
                    if player.hire_adventurer(adv):
                        output[constants.UNICODE_DIGITS.index(reaction.emoji)] = \
                            "Level {} {} | HIRED".format(adv["level"], player.stagecoach.get_class(adv["advID"]))
                        await msg.edit(embed=util.make_embed(ctx, "\n".join(output)))
                        react.pop(reaction.emoji)
                    else:
                        await ctx.author.send("You have reached your hero limit.")
            except asyncio.TimeoutError:
                break
        await msg.edit(embed=util.make_embed(ctx, "**CLOSED**"))

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
