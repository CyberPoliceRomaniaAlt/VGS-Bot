import os
import discord
from discord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!vgs", intents=intents)

@bot.event
async def on_ready():
    print(f"[VGS] Online ca {bot.user}")

TOKEN = os.getenv("TOKEN")

if not TOKEN:
    raise RuntimeError("TOKEN nu este setat!")

bot.run(TOKEN)
