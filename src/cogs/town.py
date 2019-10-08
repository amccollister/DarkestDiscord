import asyncio
import src.utils as util
import src.constants as constants

from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType
from src.classes.Player import Player
from src.classes.Stagecoach import Stagecoach

"""
A town is a single channel on a guild.
Only town commands may be performed within.

Commands:

"""
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
        dungeon = self.bot.get_dungeon(ctx.guild.id)
        channel = self.bot.get_channel(dungeon.info["town_channel"])
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
        player = self.bot.get_player(ctx.author.id)
        adv_list = player.stagecoach.adv_list
        react = util.generate_react_list(adv_list)
        msg = await util.react_send(ctx, react.keys(), fields=player.stagecoach.get_stagecoach_output())
        while True:
            try:
                reaction, user = await util.wait_for_react_change(ctx, msg, constants.STAGECOACH_REACT_TIME_LIMIT)
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
        player = self.bot.get_player(ctx.author.id)
        default_state = True
        selected_hero = None
        if not player.roster:
            return await util.send(ctx, "You have no heroes in your roster.")
        output = [hero.get_basic_info(index) for index, hero in enumerate(player.roster)]
        react = util.generate_react_list(player.roster)
        msg = await util.react_send(ctx, react.keys(), fields=output, thumbnail=ctx.author.avatar_url)
        while True:
            try:
                reaction, user = await util.wait_for_react_change(ctx, msg, constants.ROSTER_REACT_TIME_LIMIT)
                if default_state:# and reaction.emoji in react.keys():
                    if reaction.emoji in react.keys():
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
        player = self.bot.get_player(ctx.author.id)
        row = player.info
        profile = [[key, row[key]] for key in row.keys()]
        profile.pop(0)
        await util.send(ctx, fields=profile, thumbnail=ctx.author.avatar_url)

    @commands.command()
    async def upgrade(self, ctx):
        default_state = True
        player = self.bot.get_player(ctx.author.id)
        react_list = util.generate_react_list(constants.BUILDINGS.keys())
        buildings = [[k, v] for k, v in react_list.items()]
        msg = await util.react_send(ctx, react_list.keys(), "Select the building you wish to upgrade", buildings)
        await msg.add_reaction(constants.UNICODE_DIRECTIONAL["RETURN"])
        while True:
            try:
                reaction, user = await util.wait_for_react_change(ctx, msg, constants.UPGRADE_REACT_TIME_LIMIT)
                if default_state and reaction.emoji in react_list.keys():
                    chosen_building = constants.BUILDINGS[react_list[reaction.emoji]]
                    upgrade_react_list = util.generate_react_list(chosen_building)
                    fields = [["{} {}".format(constants.UNICODE_DIGITS[i], upgrade), player.get_building_cost_string(upgrade)]
                              for i, upgrade in enumerate(chosen_building)]
                    await msg.edit(embed=util.make_embed(ctx.command, "Select the upgrade you wish to improve", fields))
                    default_state = False
                elif not default_state:
                    if reaction.emoji == constants.UNICODE_DIRECTIONAL["RETURN"]:
                        await msg.edit(embed=util.make_embed(ctx.command, "Select the building you wish to upgrade", buildings))
                        default_state = True
                    elif reaction.emoji in upgrade_react_list.keys():
                        chosen_upgrade = upgrade_react_list[reaction.emoji]
                        if not player.check_afford_building_cost(chosen_upgrade):
                            await ctx.author.send("You cannot afford this upgrade!")
                        else:
                            if player.level_up(chosen_upgrade):
                                [player.add_resource(key, int(value) * -1) for key, value in player.get_building_cost(chosen_upgrade).items()]
                            fields = [["{} {}".format(constants.UNICODE_DIGITS[i], upgrade), player.get_building_cost_string(upgrade)]
                                      for i, upgrade in enumerate(chosen_building)]
                            await msg.edit(embed=util.make_embed(ctx.command, "Select the upgrade you wish to improve", fields))
            except:
                await msg.edit(embed=util.make_embed(ctx.command, "**CLOSED**", author=ctx.author))
                break

    @commands.command()
    async def kit(self, ctx):
        player = self.bot.get_player(ctx.author.id)
        resource = ["gold", "busts", "portraits", "deeds", "crests"]
        [player.add_resource(r, 1000) for r in resource]
        await ctx.send("Given 1000 of everything")


def setup(bot):
    bot.add_cog(TownCog(bot))
