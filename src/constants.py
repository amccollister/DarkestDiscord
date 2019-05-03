import os


BOT_AVATAR = None
BOT_TOKEN = os.getenv("DISCORD_TOKEN")
BOT_VERSION = 0.1
GITHUB_URL = "https://github.com/amccollister/DarkestDiscord"
DEFAULT_PREFIX = "dd."
DATABASE_PATH = "db/database.db"
SCHEMA_PATH = "db/schema.sql"
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

STAGECOACH_BASE_SIZE = 3
STAGECOACH_TIME_LIMIT = 120
STAGECOACH_REACT_TIME_LIMIT = 60
STAGECOACH_COOLDOWN = 600

ADVENTURER_BASE_CAPACITY = 2
ADVENTURER_MAX_LEVEL = 6

LEVEL_UP = {"max_hp": 5,
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