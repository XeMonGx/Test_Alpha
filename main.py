import discord
from discord.ext import commands

fichier = open("token.txt", "r")
TOKEN = fichier.read()
fichier.close()

intents = discord.Intents.default()
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print("Ready !")

client.run(TOKEN)
