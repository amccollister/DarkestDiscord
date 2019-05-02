import discord
import src.utils as util
from discord.ext import commands

from datetime import datetime
from src.classes.Player import Player

class DevCog(commands.Cog):
    def __init__(self, bot):
        # grab bot attributes
        self.bot = bot

    async def cog_before_invoke(self, ctx):
        if ctx.author.id != 66357688275050496:
            raise commands.CommandError(message="You may not use developer commands")

    @commands.command()
    async def users(self, ctx):
        users = self.bot.users
        await util.send(ctx, "I can see {} people".format(len(users)))

    @commands.command()
    async def get(self, ctx):
        self.bot.cur.execute("SELECT * FROM PLAYERS")
        p = self.bot.cur.fetchone()
        out = ["{} {}".format(x, p[x]) for x in p.keys()]
        output = "\n".join(out)
        await util.send(ctx, output)

    @commands.command()
    async def party(self, ctx):
        embed = discord.Embed()
        embed.set_author(name="Party status")
        embed.set_footer(text="Important information here")
        embed.set_image(url="https://upload.wikimedia.org/wikipedia/commons/6/6c/Herjangsfjorden_%26_Ofotfjorden%2C_wide%2C_2009_09.jpg")
        embed.add_field(name="\U0001f914", value="HP: 40/40\nStress: 10/100", inline=False)
        await ctx.send(embed=embed)

    @commands.command()
    async def level(self, ctx, arg1, arg2):
        await util.send(ctx, Player(self.bot, ctx.author.id).add_resources(arg1, arg2))


def setup(bot):
    bot.add_cog(DevCog(bot))
