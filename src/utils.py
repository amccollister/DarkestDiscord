import discord
import random
import src.constants as constants
from discord.ext import commands
from src.classes.Player import Player


def make_embed(ctx, text, *image):
    # https://cog-creators.github.io/discord-embed-sandbox/
    # https://discordpy.readthedocs.io/en/rewrite/ext/commands/api.html#context
    if len(str(text)) > 1024:
        text = "Error! The message was too long to deliver."
    embed = discord.Embed()
    embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
    embed.set_footer(text="Darkest Discord v0.1")
    embed.add_field(name=ctx.command, value=text, inline=True)
    if image:
        embed.set_image(url=image[0])
    return embed


async def send(ctx, text, *image):
    return await ctx.send(embed=make_embed(ctx, text, *image))


def check_guild_owner(ctx):
    check = ctx.guild.owner.id == ctx.author.id
    if not check:
        raise commands.CheckFailure(message="You must be the guild owner to use this command.")
    return check


### DB commands ###

def get_pre(bot, message):
    bot.cur.execute("SELECT prefix FROM CHANNEL WHERE guildID = {}".format(message.guild.id))
    return bot.cur.fetchone()[0]


def get_db_channel(bot, name, guild_id):
    bot.cur.execute("SELECT {}ID FROM CHANNEL WHERE guildID = {}".format(name, guild_id))
    channel_id = bot.cur.fetchone()[0]
    return bot.get_channel(channel_id)


# Adventurers are in the stagecoach. Heroes are in the party.
def get_adventurer(bot, adventurer_id):
    bot.cur.execute("SELECT * FROM ADVENTURER_LIST WHERE advID = {}".format(adventurer_id))
    return bot.cur.fetchone()

# TODO: put this somewhere appropriate
def hire_adventurer(bot, player_id, adv):
    # check if the hero is still there
    bot.cur.execute("SELECT * FROM STAGECOACH WHERE stagecoachID = {}".format(adv["stagecoachID"]))
    if not bot.cur.fetchone():
        return "The adventurer is no longer available."
    bot.cur.execute("DELETE FROM STAGECOACH WHERE stagecoachID = {}".format(adv["stagecoachID"]))
    name = get_adventurer(bot, adv["advID"])["name"]
    ins = [adv["advID"], player_id, adv["level"], name]
    bot.cur.execute("INSERT INTO HEROES (advID, playerID, level, character_name) VALUES({},{},{},\'{}\')".format(*ins))
    return "HIRED: Level {} {}".format(adv["level"], name)


def get_roster(bot, player_id):
    bot.cur.execute("SELECT * FROM HEROES WHERE playerID = {}".format(player_id))
    return bot.cur.fetchall()
