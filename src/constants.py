import os

DISCORD_MSG_LIMIT = 2000
BOT_TOKEN = os.getenv("DISCORD_TOKEN")
DEFAULT_PREFIX = "dd."
COGS = ["setup", "town", "dungeon", "dev"]

UNICODE_DIGITS = ["\U00000031\U000020e3",
                  "\U00000032\U000020e3",
                  "\U00000033\U000020e3",
                  "\U00000034\U000020e3",
                  "\U00000035\U000020e3",
                  "\U00000036\U000020e3",
                  "\U00000037\U000020e3",
                  "\U00000038\U000020e3",
                  "\U00000039\U000020e3",
                  "\U00000030\U000020e3"]

# --BASE VALUES-- #

STAGECOACH_BASE_SIZE = 4
STAGECOACH_TIME_LIMIT = 120
STAGECOACH_REACT_TIME_LIMIT = 30