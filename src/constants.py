import os

DISCORD_MSG_LIMIT = 2000
BOT_TOKEN = os.getenv("DISCORD_TOKEN")
DEFAULT_PREFIX = "dd."
COGS = ["setup", "town", "dungeon", "dev"]