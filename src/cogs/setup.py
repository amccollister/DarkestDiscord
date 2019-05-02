import src.constants as constants
import src.utils as util
from discord.ext import commands


class SetupCog(commands.Cog):
    def __init__(self, bot):
        #grab bot attributes
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        """
        Usage:
                !ping

        Tests the responsiveness of the bot.
        Pong.
        """
        await util.send(ctx, "Pong.")

    # TODO: rewrite this mess... like for real
    @commands.command()
    async def help(self, ctx, *arg):
        """
        Usage:
                !help <plugin|command>

        That's this command!
        Gives you help based on the desired plugin or command you specify.
        If no arguments are specified, it displays all available plugins.
        """
        cogs = ctx.bot.cogs
        if not arg:
            text = "__**PLUGINS**__\n"
            for cog in cogs.keys():
                text += cog[:-3] + "\n"
            return await util.send(ctx, text)
        else:
            cog = arg[0].lower().capitalize() + "Cog"
            if cog in cogs:
                command = [x.name for x in cog.get_commands()]
                text = "__**{0} Commands**__\n".format(cog[:-3])
                for c in command:
                    text += c + "\n"
                await util.send(ctx, text)
            else:
                command = arg[0].lower()
                if command in [x.name for x in ctx.bot.commands]:
                    await util.send(ctx, ctx.bot.get_command(command).help)
                else:
                    await util.send(ctx, "That plugin does not exist or is not currently installed.")

    # TODO: set_db_channel
    @commands.command()
    @commands.check(util.check_guild_owner)
    async def set_town(self, ctx):
        util.set_db_channel(ctx.bot, "town", ctx.channel.id, ctx.guild.id)
        await util.send(ctx, "This is now the town channel.")

    @commands.command()
    @commands.check(util.check_guild_owner)
    async def set_dungeon(self, ctx):
        util.set_db_channel(ctx.bot, "dungeon", ctx.channel.id, ctx.guild.id)
        await util.send(ctx, "This is now the dungeon channel.")

    @commands.command()
    @commands.check(util.check_guild_owner)
    async def set_prefix(self, ctx, arg):
        print(arg)
        if any(ch in arg for ch in [" ", "\'", "\""]):
            raise commands.CommandError(message="The prefix cannot have spaces, \', or \".")
        ctx.bot.db.update_row("CHANNEL", "prefix = '{}'".format(arg), "guildID = {}".format(ctx.guild.id))
        await util.send(ctx, "The prefix has been set to {}".format(arg))

    @commands.command()
    async def town(self, ctx):
        channel = util.get_db_channel(self.bot, "town", ctx.guild.id)
        if not channel:
            return await util.send(ctx, "The town has not been set.")
        await util.send(ctx, "The town can be found at: {}".format(channel.mention))

    @commands.command()
    async def dungeon(self, ctx):
        channel = util.get_db_channel(self.bot, "town", ctx.guild.id)
        if not channel:
            return await util.send(ctx, "The dungeon has not been set.")
        await util.send(ctx, "The dungeon can be found at: {}".format(channel.mention))


def setup(bot):
    bot.add_cog(SetupCog(bot))
