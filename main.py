import discord
from discord.ext import commands
import asyncio

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents, help_command=None)

@bot.event
async def on_ready():
    pass

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.content.strip() == '!clear':
        try:
            deleted = await message.channel.purge(limit=100)
            conf = await message.channel.send(f'✅ Cleared {len(deleted)} messages!')
            await asyncio.sleep(3)
            await conf.delete()
        except:
            await message.channel.send('Error clearing messages!')
    await bot.process_commands(message)

with open("token.txt") as token:
    bot.run(token.readline())