import discord
from discord.ext import commands
from discord import app_commands

from utils.database import get_game, get_all_games
from utils.embeds import create_game_embed
from utils.views import LinkView


class Game(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    async def game_autocomplete(
        self,
        interaction: discord.Interaction,
        current: str
    ):

        games = get_all_games()

        return [
            app_commands.Choice(
                name=name,
                value=name
            )
            for name in games.keys()
            if current.lower() in name.lower()
        ][:25]

    @app_commands.command(
        name="game",
        description="Show a saved game."
    )
    @app_commands.autocomplete(name=game_autocomplete)
    async def game(
        self,
        interaction: discord.Interaction,
        name: str
    ):

        data = get_game(name)

        if data is None:
            await interaction.response.send_message(
                "❌ Game not found.",
                ephemeral=True
            )
            return

        embed = create_game_embed(name, data)

        view = LinkView(data["link"])

        await interaction.response.send_message(
            embed=embed,
            view=view
        )


async def setup(bot):
    await bot.add_cog(Game(bot))
