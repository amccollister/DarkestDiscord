import random
import src.utils as util
from discord.ext import commands


class TownCog(commands.Cog):
    def __init__(self, bot):
        # grab bot attributes
        self.bot = bot

        # Town Background Tasks
        # TODO: random timed adventurers in stagecoach unique to each player
        # self.stagecoach_refresh = self.bot.loop.create_task(self.refresh_stagecoach())

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
        total = random.randint(1, 6)
        self.bot.cur.execute("SELECT * FROM ADVENTURER_LIST")
        heroes = self.bot.cur.fetchall()
        output = "Available Heroes:"
        for i in range(total):
            output += "\n"
            output += "{}. ".format(i+1) + random.choice(heroes)[1] + " | Level {}".format(random.randint(0, 6))
        await util.send(ctx, output)

    @commands.command()
    async def roster(self, ctx):
        await util.send(ctx, "This will display your roster")


def setup(bot):
    bot.add_cog(TownCog(bot))
