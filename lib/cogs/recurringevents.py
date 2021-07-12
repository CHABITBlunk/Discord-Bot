from discord.ext.commands import Cog
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
from lib.db import db
import random
from discord import File

class RecurringEvents(Cog):
    def __init__(self, bot):
        self.bot = bot
        self.scheduler = AsyncIOScheduler()
        db.autosave(self.scheduler)

    async def ball_inspection(self):
        await self.bot.stdout.send('DAILY MANDATORY BALL INSPECTION')
        rand = random.randint(1, 7)
        await self.bot.stdout.send(file=File(f'./gifs/inspection-{rand}.gif'))

    async def futurehokage_reminder(self):
        await self.bot.stdout.send('weekly reminder that futurehokage is a ***BITCH***')

    @Cog.listener()
    async def on_ready(self):
        self.scheduler.add_job(self.ball_inspection, CronTrigger(hour=12, minute=0, second=0))
        self.scheduler.add_job(self.futurehokage_reminder, CronTrigger(day_of_week=0, hour=0, minute=0, second=0))
        self.scheduler.start()

def setup(bot):
    bot.add_cog(RecurringEvents(bot))
