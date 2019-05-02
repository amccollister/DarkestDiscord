import discord

from discord.ext import commands


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


async def react_send(ctx, text, reactions, *image):
    msg = await send(ctx, text, *image)
    for emote in reactions:
        await msg.add_reaction(emote)
    return msg


def check_guild_owner(ctx):
    check = ctx.guild.owner.id == ctx.author.id
    if not check:
        raise commands.CheckFailure(message="You must be the guild owner to use this command.")
    return check


### DB commands ###

def get_pre(bot, message):
    row = bot.db.get_row("CHANNEL", "guildID", message.guild.id)
    return row["prefix"]


def get_db_channel(bot, name, guild_id):
    row = bot.db.get_row("CHANNEL", "guildID", guild_id)
    return bot.get_channel(row["{}ID".format(name)])


def set_db_channel(bot, name, channel_id, guild_id):
    bot.db.update_row("CHANNEL", "{}ID = {}".format(name, channel_id), "guildID = {}".format(guild_id))


def get_roster(bot, player_id):
    return bot.db.get_row("HEROES", "playerID", player_id)
