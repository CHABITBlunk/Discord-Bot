import discord
import random
from discord.ext import commands

BALL_INSPECTOR_TOKEN = 'NzYyMDUxNjYxMTIwMDEyMjg4.X3jh6g.ieHlqN2ixewNYeED4i-Do4KnBmE'

bot = commands.Bot(command_prefix='.')

@bot.event
async def on_ready():
    print('Logged in as {0}!'.format(bot.user))

@bot.event
async def on_message(ctx):
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
    print('this workie')
    await ctx.channel.send(arg)

bot.run(BALL_INSPECTOR_TOKEN)