import discord

from config import EMBED_COLOR, FOOTER_TEXT


def create_game_embed(game_name: str, data: dict):

    embed = discord.Embed(
        title=f"🎮 {game_name}",
        color=EMBED_COLOR
    )

    embed.add_field(
        name="🟢 Status",
        value=data["status"],
        inline=False
    )

    embed.add_field(
        name="🎁 Event",
        value=data["event"],
        inline=False
    )

    if data.get("event_key"):
        embed.add_field(
            name="🔑 Event Key",
            value=data["event_key"],
            inline=False
        )

    embed.set_footer(text=FOOTER_TEXT)

    return embed
