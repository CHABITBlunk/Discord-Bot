import random
from discord import File
from discord import Embed
from discord.ext.commands import Bot as BotBase
from discord.ext.commands import CommandNotFound
from glob import glob
from asyncio import sleep

PREFIX = '.'
OWNER_IDS = [4660158167480576]
COGS = [path.split('/')[-1][:-3] for path in glob('./lib/cogs/*.py')]

class Ready(object):
    def __init__(self):
        for cog in COGS:
            setattr(self, cog, False)

    def ready_up(self, cog):
        setattr(self, cog, True)
        print(f'{cog} ready')

    def all_ready(self):
        return all([getattr(self, cog) for cog in COGS])

class Bot(BotBase):
    def __init__(self):
        self.ready = False
        self.cogs_ready = Ready()
        self.guild = None
        self.PREFIX = PREFIX
        super().__init__(
                command_prefix=PREFIX, 
                owner_ids=OWNER_IDS
        )

    def setup(self):
        for cog in COGS:
            self.load_extension(f'lib.cogs.{cog}')
            print(f'{cog} loaded')
    
    def run(self, version):
        self.VERSION = version
        print('running setup...')
        self.setup()
        with open('./lib/bot/token.0', 
                'r', 
                encoding='utf-8') as tf:
            self.TOKEN = tf.read()
        print('running bot...')
        super().run(self.TOKEN, reconnect=True)

    async def on_connect(self):
        print('bot connected')
    
    async def on_disconnect(self):
        print('bot disconnected')

    async def on_error(self, err, *args, **kwargs):
        raise 

    async def on_command_error(self, ctx, exc):
        if isinstance(exc, CommandNotFound):
            pass
        else:
            raise exc.original

    async def on_ready(self):
        if not self.ready:
            self.guild = self.get_guild(856408164793450506)
            self.stdout = self.get_channel(864003308225429504)
            while not self.cogs_ready.all_ready():
                await sleep(0.25)
            self.ready = True
            print('bot ready')
            
        else:
            print('bot reconnected')

bot = Bot()
