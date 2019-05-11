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
        if not ctx.guild:
            return True
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
        # TODO: make this better. Put the complex stuff in Stagecoach object
        player = Player(ctx.bot, ctx.author.id)
        adv_list = player.stagecoach.adv_list
        react = util.generate_react_list(adv_list)
        msg = await util.react_send(ctx, react.keys(), fields=player.stagecoach.get_stagecoach_output())
        while True:
            try:
                reaction, user = await ctx.bot.wait_for("reaction_add",
                                                        check=lambda r, u: u.id == ctx.author.id and r.message.id == msg.id,
                                                        timeout=constants.STAGECOACH_REACT_TIME_LIMIT)
                if reaction.emoji in react.keys():
                    adv = react[reaction.emoji]
                    if player.hire(adv):
                        await msg.edit(embed=util.make_embed(ctx.command, fields=player.stagecoach.get_stagecoach_output(), author=ctx.author))
                        react.pop(reaction.emoji)
                    else:
                        await ctx.author.send("You have reached your hero limit.")
            except asyncio.TimeoutError:
                await msg.edit(embed=util.make_embed(ctx.command, "**CLOSED**", author=ctx.author))
                break

    @commands.command()
    async def roster(self, ctx):
        player = Player(ctx.bot, ctx.author.id)
        default_state = True
        selected_hero = None
        if not player.roster:
            return await util.send(ctx, "You have no heroes in your roster.")
        output = [hero.get_basic_info(index) for index, hero in enumerate(player.roster)]
        react = util.generate_react_list(player.roster)
        msg = await util.react_send(ctx, react.keys(), fields=output, thumbnail=ctx.author.avatar_url)
        while True:
            try:
                reaction, user = await ctx.bot.wait_for("reaction_add",
                                                        check=lambda r, u: u.id == ctx.author.id and r.message.id == msg.id,
                                                        timeout=constants.ROSTER_REACT_TIME_LIMIT)
                if default_state and reaction.emoji in react.keys():
                    default_state = False
                    selected_hero = react[reaction.emoji]
                    await msg.edit(embed=selected_hero.get_detailed_info())
                    await msg.add_reaction(constants.UNICODE_DIRECTIONAL["RETURN"])
                    await msg.add_reaction(constants.UNICODE_DIRECTIONAL["FIRE"])
                else:
                    if reaction.emoji == constants.UNICODE_DIRECTIONAL["RETURN"]:
                        output = [hero.get_basic_info(index) for index, hero in enumerate(player.roster)]
                        await msg.edit(embed=util.make_embed(ctx.command, fields=output, author=ctx.author))
                        default_state = True
                        selected_hero = None
                    elif reaction.emoji == constants.UNICODE_DIRECTIONAL["FIRE"]:
                        await util.send(ctx, "Please type 'confirm' to fire {}, otherwise type 'cancel'".format(selected_hero.info["name"]), dm=True)
                        confirmation = await ctx.bot.wait_for("message",
                                                              check=lambda x: x.author.id == ctx.author.id and not x.guild)
                        if confirmation.content.lower() == "confirm":
                            if player.fire(selected_hero):
                                await util.send(ctx, "{} has been let go.".format(selected_hero.info["name"]), dm=True)
                                react = util.generate_react_list(player.roster)
                            else:
                                await util.send(ctx, "The hero has already been let go.", dm=True)
                            default_state = True
                            selected_hero = None
                            output = [hero.get_basic_info(index) for index, hero in enumerate(player.roster)]
                            await msg.edit(embed=util.make_embed(ctx.command, fields=output, author=ctx.author))
                        else:
                            await util.send(ctx, "Operation cancelled.", dm=True)
            except asyncio.TimeoutError:
                output = [hero.get_basic_info(index) for index, hero in enumerate(player.roster)]
                await msg.edit(embed=util.make_embed(ctx.command, fields=output, author=ctx.author, thumbnail=ctx.author.avatar_url))
                break

    @commands.command()
    async def profile(self, ctx):
        row = Player(ctx.bot, ctx.author.id).info
        profile = [[key, row[key]] for key in row.keys()]
        profile.pop(0)
        await util.send(ctx, fields=profile, thumbnail=ctx.author.avatar_url)


def setup(bot):
    bot.add_cog(TownCog(bot))
