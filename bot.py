import discord
import random
from discord.ext import commands
import os

BALL_INSPECTOR_TOKEN = ''
if os.path.isfile('home/pi/discord-token.txt'):
    txt_file = open('/home/pi/discord-token.txt', 'r')
    BALL_INSPECTOR_TOKEN = txt_file.read()
    txt_file.close()

bot = commands.Bot(command_prefix='.')

@bot.event
async def on_ready():
    print('Logged in as {0}!'.format(bot.user))

@bot.event
async def on_message(ctx):
    await bot.process_commands(ctx)
    if (ctx.author == bot.user):
        return
    if (ctx.content.lower().startswith('hey')):
        await ctx.channel.send('hey shartie wussup :smiling_face_with_3_hearts: :cold_face:')

@bot.event
async def on_join(user, ctx):
    rand = random.randint(1, 7)
    file = discord.File('./gifs/inspection-{0}.gif'.format(rand))
    await ctx.send(message=user.mention, file=file)

@bot.command()
async def test(ctx, *, arg):
    await ctx.channel.send(arg)

bot.run(BALL_INSPECTOR_TOKEN)
