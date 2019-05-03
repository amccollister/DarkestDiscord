import discord
import src.constants as constants
from discord.ext import commands


def make_embed(title=None, description=None, fields=None, image=None, thumbnail=None, author=None):
    # https://discordpy.readthedocs.io/en/rewrite/api.html#discord.Embed
    # https://discordpy.readthedocs.io/en/latest/faq.html#how-do-i-use-a-local-image-file-for-an-embed-image
    embed_title = title or ""
    embed_description = description or ""
    # TODO: dynamic color adjustments
    embed = discord.Embed(title=str(embed_title), description=str(embed_description), color=0xc40000)
    embed.set_author(name=author.name, icon_url=author.avatar_url)
    embed.set_footer(text="Darkest Discord v{}".format(constants.BOT_VERSION), icon_url=constants.BOT_AVATAR)
    embed.set_image(url=image) if image else None
    embed.set_thumbnail(url=thumbnail) if thumbnail else None
    [embed.add_field(name=field[0], value=field[1], inline=True) for field in fields] if fields else None
    return embed


async def send(ctx, description=None, fields=None, image=None, thumbnail=None, author=None):
    auth = author or ctx.author
    icon = ctx.bot.user.avatar_url
    return await ctx.send(embed=make_embed(ctx.command, description, fields, image, thumbnail, auth))


async def react_send(ctx, description, reactions, fields=None, image=None, thumbnail=None, author=None):
    msg = await send(ctx, description, fields, image, thumbnail, author)
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
