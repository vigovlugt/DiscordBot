import discord
from discord.ext.commands import bot
from discord.ext import commands
import math
import random
import time

Client = discord.Client()
bot_prefix = "/"
client = commands.Bot(command_prefix=bot_prefix)

@client.event
async def on_ready():
    print("Bot Online!")
    print("Name: {}".format(client.user.name))
    print("ID: {}".format(client.user.id))

@client.command(pass_context=True)
async def Ping(ctx):
    await client.say("pong motherfucker")


client.run("Mzc5MDAxMDQ2MjcxMjYyNzIy.DOjryA.K8m8wRchmjbq3v-Ty0pBYrmgd9g")