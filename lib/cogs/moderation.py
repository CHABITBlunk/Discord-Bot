from discord.ext.commands import Cog
from discord.ext.commands import command
from discord.ext.commands import has_permissions
import discord

class Moderation(Cog):
    def __init__(self, bot):
        self.bot = bot

    @command(help='this command will ban members')
    @has_permissions(ban_members=True)
    async def ban(self, ctx, member:discord.User=None, *, reason=None):
        if member == None:
            await ctx.channel.send('whomst\'d\'ve do i ban b0ss')
            return
        if member == ctx.message.author:
            await ctx.channel.send('you can\'t ban yourself b0ss')
            return
        if reason == None:
            reason = 'bein a dick idk man'
        await member.send(f'you got banned from {ctx.guild.name} for {reason}')
        await member.ban(reason=reason)
        await ctx.send(f'{member} has done did been banno moded')

    @command(help='this command will unban members')
    @has_permissions(ban_members=True)
    async def unban(self, ctx, *, member=None):
        if member == None:
            await ctx.channel.send('whomst\'d\'ve do i unban b0ss')
            return
        if member == ctx.message.author:
            await ctx.channel.send('you can\'t unban yourself dumbass you\'re part of this server')
            return
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user
            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f'unbanned{user.mention}')
                await user.send(f'you\'ve been unbanned from {ctx.guild}')
                return

    @command(help='this command will kick members')
    @has_permissions(kick_members=True)
    async def kick(self, ctx, member:discord.Member=None, *, reason=None):
        if member == None:
            await ctx.channel.send('whomst\'d\'ve do i kick b0ss')
            return
        if member == ctx.message.author:
            await ctx.channel.send('you can\'t kick yourself b0ss')
            return
        if reason == None:
            reason = 'bein a dick idk man'
        await member.kick(reason=reason)
        await ctx.send(f'{member} has done did been kicko moded')

    @command(help='this command will remove a specified amount of messages, with a default of 5')
    @has_permissions(manage_messages=True)
    async def clear(self, ctx, amount=5):
        amount += 1
        await ctx.channel.purge(limit=amount)

def setup(bot):
    bot.add_cog(Moderation(bot))
