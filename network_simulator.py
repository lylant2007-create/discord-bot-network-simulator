import discord
from discord.ext import commands
import random
import asyncio

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user} is ready!")

@bot.command()
async def watch(ctx):
    await ctx.send("💻 Checking your network...")
    await asyncio.sleep(2)

    ip = f"192.168.0.{random.randint(1,255)}"
    devices = random.randint(1,5)

    status = random.choice([
        "🟢 Safe",
        "🟡 Suspicious activity",
        "🔴 Being watched 👁️",
        "⚠️ Unknown device detected"
    ])

    await ctx.send(f"""
IP: {ip}
Devices connected: {devices}

Status: {status}
""")
bot.run("ur token")
