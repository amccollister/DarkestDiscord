import sys
import src.constants as constants

from discord.ext.commands import Bot


class DarkestBot(Bot):
    # on_member_join on_member_remove
    # on_member_update on_member_ban on_guild_join
    # on_command on_command_error on_command_completion
    def __init__(self):
        super().__init__(constants.PREFIX)
        self.remove_command('help')  # We will be implementing our own.

    def run(self):
        super().run(constants.BOT_TOKEN)

    async def on_ready(self):
        print("------------")
        print("Logged in as")
        print(self.user.name)
        print(self.user.id)
        print("------------")
        self.load_extension("src.chat")
        #for plugin in constants.PLUGINS:
        #    self.load_extension("src.{}".format(plugin))

    async def on_message(self, message):
        #str_id = str(message.channel.id)
        if message.author.id != self.user.id:
            print("Message from {0.author}: {0.content}".format(message))
        await self.process_commands(message)
        #if constants.WHITELIST and str_id in constants.WHITELIST:
        #    await self.process_commands(message)
        #elif str_id not in constants.BLACKLIST:
        #    await self.process_commands(message)

    async def on_error(self, event, *args, **kwargs):
        print(sys.exc_info())
        print("ERROR: {}".format(event))
