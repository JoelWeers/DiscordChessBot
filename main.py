# This code is based on the following example:
# https://discordpy.readthedocs.io/en/stable/quickstart.html#a-minimal-bot

import os

import discord

from dotenv import load_dotenv
load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

board = '\u25FCabcdefg\n1\u265C\u265E\u265D\u265B\u265A\u265D\u265E\u265C\n2\u265F\u265F\u265F\u265F\u265F\u265F\u265F\u265F\n3\u2795\u2573\u2795\u2573\u2795\u2573\u2795\u2573\n4'

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
    
    if message.content.startswith('/start'):
        await message.channel.send('Let the game commence!\u2588\u2001\u2588\u2001\u2588\u2001\u2588\u2001')

    if message.content.startswith('/board'):
        await message.channel.send(board)

token = os.getenv('TOKEN')
client.run(token)

