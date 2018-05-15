import discord

from redbot.core import Config, checks, commands

from redbot.core.bot import Red


class MyCog:
    """
    V3 Cog Template
    """

    def __init__(self, bot: Red):
        self.bot = bot
        self.config = Config.get_conf(self, identifier=826968, force_registration=True)
        default_global = {}
        default_guild = {}

        self.config.register_global(**default_global)
        self.config.register_guild(**default_guild)

    @commands.command()
    async def mycommand(self, ctx: commands.Context):
        """
       My custom cog
       
       Extra information goes here after two newlines
       **This part** supports ~~discord~~ `Markdown`
       """
        await ctx.send("Hello World")
