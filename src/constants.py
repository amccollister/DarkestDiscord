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


ADVENTURER_MAX_LEVEL = 6

LEVEL_UP = {"hp": 5,
            "dodge": 5,
            "prot": 5,
            "spd": 5,
            "acc": 5,
            "crit": 5,
            "dmg_lower": 5,
            "dmg_upper": 5,
            "stun_res": 10,
            "blight_res": 10,
            "disease_res": 10,
            "death_blow_res": 10,
            "move_res": 10,
            "bleed_res": 10,
            "debuff_res": 10,
            "trap_res": 10}