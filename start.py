import src.constants as constants
from src.bot import DarkestBot


def main():
    bot = DarkestBot()
    for plugin in constants.COGS:
        bot.load_extension("src.{}".format(plugin))
    bot.run()


if __name__ == "__main__":
    main()
