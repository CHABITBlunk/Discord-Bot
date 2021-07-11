import discord
import random
from discord.ext import commands
import youtube_dl
import os

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
async def on_join(member):
    rand = random.randint(1, 7)
    print(str(rand))
    gif = discord.File('./gifs/inspection-{0}.gif'.format(rand))
    await member.channel.send('welcome to hell {0}'.format(user.mention))
    await member.channel.send(file=gif)

@bot.command()
async def join(ctx):
    channel = ctx.author.voice.channel
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    await channel.connect()
    await ctx.channel.send('joined **{0}** successfully'.format(channel))

@bot.command()
async def play(ctx, url: str):
    songIsThere = os.path.isfile('song.mp3')
    try:
        if songIsThere:
            os.remove('song.mp3')
    except PermissionError:
        await ctx.send('wait for the music to finish or use the **stop** command')
    await join(ctx)
    ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }]
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    for file in os.listdir('./'):
        if file.endswith('.mp3'):
            os.rename('song.mp3')
    voice.play(discord.FFmpegPCMAudio('song.mp3')

@bot.command()
async def pause(ctx):
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    if voice.is_playing():
        voice.pause()
    else:
        await ctx.send('no audio be playin')

@bot.command()
async def resume(ctx):
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    if voice.is_paused():
        voice.resume()
    else:
        await ctx.send('no audio to pause')

@bot.command()
async def stop(ctx):
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    voice.stop()

@bot.command()
async def leave(ctx):
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    await ctx.voice_client.disconnect()

bot.run(BALL_INSPECTOR_TOKEN)
