from discord import User
from discord.ext.commands import Cog

class Events(Cog):
    def __init__(self, bot):
        self.bot = bot

    @Cog.listener()
    async def on_message(self, ctx):
        if not ctx.author == self.bot.user and ctx.content.lower().startswith('hey'):
            await ctx.channel.send('hey shartie wussup :smiling_face_with_3_hearts: :cold_face:')
    
    @Cog.listener()
    async def on_join(member:User, ctx):
        await ctx.channel.send(f'welcome to hell {member.mention}')

def setup(bot):
    bot.add_cog(Events(bot))
