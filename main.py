import discord
from discord.ext import commands

fichier = open("token.txt", "r")
TOKEN = fichier.read()
fichier.close()

intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix='$', intents=intents)


@client.event
async def on_ready():
    print("Ready !")


@client.command()
async def help_cmd(ctx):
    await ctx.send('$spam [numbre] [text]: Je peut spam au plus 10 fois')


@client.command()
async def test(ctx, args):
    if args == 'bonjour':
        await ctx.send('Bonjour!')
    else:
        await ctx.send('ok')


@client.command()
async def spam(ctx, a: int, args):
    await ctx.message.delete()
    if a <= 10:
        for i in range(a-1):
            await ctx.channel.send(args, delete_after=1.0)
        confirm = discord.Embed(title='Spam reussi!', description=f'Spam {args} #{ctx.channel}', color=0x4fff4d)
        await ctx.channel.send(embed=confirm, delete_after=10.0)
    else:
        message = discord.Embed(title='Weeeesh un peut trop là non!', color=0x4fff4d)
        await ctx.channel.send(embed=message, delete_after=10.0)


@client.command()
async def add(ctx, a: int, b: int):
    await ctx.send(a + b)


client.run(TOKEN)
