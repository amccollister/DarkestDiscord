import logging
import src.constants as constants
from src.bot import DarkestBot


def main():
    start_logging()
    bot = DarkestBot()
    for plugin in constants.COGS:
        bot.load_extension("src.cogs.{}".format(plugin))
    bot.run()


def start_logging():
    logger = logging.getLogger('discord')
    logger.setLevel(logging.DEBUG)
    handler = logging.FileHandler(filename="db/bot.log", encoding="utf-8", mode="w")
    handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
    logger.addHandler(handler)


if __name__ == "__main__":
    main()
