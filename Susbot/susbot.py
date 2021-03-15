import os
import discord
import random
from dotenv import load_dotenv

load_dotenv()
TOKEN = 'ODIxMTUyODMxOTQyODE5ODYx.YE_kKw.SwdS4SL_VBYkSRCLMtLI6NnFXmQ'

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'{member.name}, you lookin real sussy'
    )
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    airpod_shotty_quotes =[
        'Airpod shotty, I\'mma catch a body',
        'You lookin real sussy'
        ]
    
    if message.content == 'airpod shotty':
        response = random.choice(airpod_shotty_quotes)
        await message.channel.send(response)
    if message.content == 'AirPod shotty':
        response = random.choice(airpod_shotty_quotes)
        await message.channel.send(response)
    if message.content == 'Airpod shotty':
        response = random.choice(airpod_shotty_quotes)
        await message.channel.send(response)
    if message.content == 'Airpod shawty':
        response = random.choice(airpod_shotty_quotes)
        await message.channel.send(response)
    if message.content == 'airpod shawty':
        response = random.choice(airpod_shotty_quotes)
        await message.channel.send(response)
client.run(TOKEN)
