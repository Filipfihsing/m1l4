import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Zalogowaliśmy się jako {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Cześć, jestem bot{bot.user}!')

@bot.command()
async def heh(ctx, text, count_heh = 5):
    await ctx.send((text +" ") * count_heh)
    
    
@bot.event
async def on_message_edit(before, after):
    if before.author == bot.user:
        return
    
    await before.channel.send("Przed modyfikacją: " + before.content + "\nPo modyfikacji: " + after.content)


bot.run
