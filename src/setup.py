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

    @commands.command()
    async def help(self, ctx, *arg):
        """
        Usage:
                !help <plugin|command>

        That's this command!
        Gives you help based on the desired plugin or command you specify.
        If no arguments are specified, it displays all available plugins.
        """
        cogs = ctx.bot.cogs.keys()
        if not arg:
            text = "__**PLUGINS**__\n"
            for cog in ctx.bot.cogs.keys():
                text += cog[:-3] + "\n"
            return await util.send(ctx, text)
        else:
            cog = arg[0].lower().capitalize() + "Cog"
            if cog in cogs:
                command = [x.name for x in ctx.bot.get_cog_commands(cog)]
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

    @commands.command() #guild owner only
    async def set_town(self, ctx):
        await util.send(ctx, "Town channel has been set!")

    @commands.command() #guild owner only
    async def set_dungeon(self, ctx):
        await util.send(ctx, "Dungeon channel has been set!")

    @commands.command()  # guild owner only (sanitize that input kiddo)
    async def set_prefix(self, ctx, arg):
        await util.send(ctx, "Prefix has been set to {}")

    @commands.command() #guild owner only
    async def town(self, ctx):
        await util.send(ctx, "The town is located at <insert reference here>")

    @commands.command() #guild owner only
    async def dungeon(self, ctx):
        await util.send(ctx, "The dungeon is located at <insert reference here>!")



def setup(bot):
    bot.add_cog(SetupCog(bot))
