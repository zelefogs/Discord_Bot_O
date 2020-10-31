import discord
import re

from discord.ext import commands

from config import settings
from utils import weather
from utils import make_bin_string
from utils import Joke_Parser
from config import OWM_API_KEY


client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    msg = message.content
    if message.author == client.user:
        return

    if message.content.startswith('$weather'):
        try:
            city = (' '.join(msg.split(' ')[1:])).title()
            await message.channel.send(weather(city))
        except Exception as e:
            await message.channel.send('Город не найден')

    if message.content.startswith('$binstr'):
        text_str = ' '.join(msg.split(' ')[1:])
        res = re.search(r'\S+', text_str)
        if res is None:
            await message.channel.send(f'Вы ввели пустую строку')
            return
        else:
            str_result = make_bin_string(res[0])
            await message.channel.send(str_result)

    if message.content.startswith('$joke'):
        joke = Joke_Parser()
        await message.channel.send(joke.get_joke())
client.run(settings['token'])

