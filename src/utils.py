import discord
from discord.ext import commands


def make_embed(ctx, text, *image):
    # https://cog-creators.github.io/discord-embed-sandbox/
    # https://discordpy.readthedocs.io/en/rewrite/ext/commands/api.html#context
    if len(str(text)) > 1024:
        text = "Error! The message was too long to deliver. Please shorten the next input."
    embed = discord.Embed()
    embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
    embed.set_footer(text="Darkest Discord v0.1")
    embed.add_field(name=ctx.command, value=text, inline=True)
    if image:
        embed.set_image(url=image[0])
    return embed


async def send(ctx, text, *image):
    await send_embed(ctx, embed=make_embed(ctx, text, *image))


async def send_embed(ctx, embed):
    await ctx.send(embed=embed)


def check_guild_owner(ctx):
    check = ctx.guild.owner.id == ctx.author.id
    if not check:
        raise commands.CheckFailure(message="You must be the guild owner to use this command.")
    return check


def get_pre(bot, message):
    bot.cur.execute("SELECT prefix FROM CHANNEL WHERE guildID = {}".format(message.guild.id))
    return bot.cur.fetchone()[0]


def get_db_channel(bot, name, guild_id):
    bot.cur.execute("SELECT {}ID FROM CHANNEL WHERE guildID = {}".format(name, guild_id))
    channel_id = bot.cur.fetchone()[0]
    return bot.get_channel(channel_id)
