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
        await util.send(ctx, "This will be useful at some point")

    @commands.command()
    @commands.check(util.check_guild_owner)
    async def set_town(self, ctx):
        dungeon = self.bot.get_dungeon(ctx.guild.id)
        dungeon.set_channel("town", ctx.channel.id)
        # util.set_db_channel(ctx.bot, "town", ctx.channel.id, ctx.guild.id)
        await util.send(ctx, "This is now the town channel.")

    @commands.command()
    @commands.check(util.check_guild_owner)
    async def set_dungeon(self, ctx):
        dungeon = self.bot.get_dungeon(ctx.guild.id)
        dungeon.set_channel("dungeon", ctx.channel.id)
        # util.set_db_channel(ctx.bot, "dungeon", ctx.channel.id, ctx.guild.id)
        await util.send(ctx, "This is now the dungeon channel.")

    @commands.command()
    @commands.check(util.check_guild_owner)
    async def set_prefix(self, ctx, arg):
        dungeon = self.bot.get_dungeon(ctx.guild.id)
        if any(ch in arg for ch in [" ", "\'", "\""]):
            raise commands.CommandError(message="The prefix cannot have spaces, \', or \".")
        dungeon.set_prefix(arg)
        # ctx.bot.db.update_row("CHANNEL", "prefix = '{}'".format(arg), "guildID = {}".format(ctx.guild.id))
        await util.send(ctx, "The prefix has been set to {}".format(arg))

    @commands.command()
    async def town(self, ctx):
        # change to dungeon object
        # channel = util.get_db_channel(self.bot, "town", ctx.guild.id)
        dungeon = self.bot.get_dungeon(ctx.guild.id)
        channel = self.bot.get_channel(dungeon.info["town_channel"])
        if not channel:
            return await util.send(ctx, "The town has not been set.")
        await util.send(ctx, "The town can be found at: {}".format(channel.mention))

    @commands.command()
    async def dungeon(self, ctx):
        # change to dungeon object
        # channel = util.get_db_channel(self.bot, "town", ctx.guild.id)
        dungeon = self.bot.get_dungeon(ctx.guild.id)
        channel = self.bot.get_channel(dungeon.info["dungeon_channel"])
        if not channel:
            return await util.send(ctx, "The dungeon has not been set.")
        await util.send(ctx, "The dungeon can be found at: {}".format(channel.mention))


def setup(bot):
    bot.add_cog(SetupCog(bot))
