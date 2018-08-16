import discord
from discord.ext import commands

import config

startup_extensions = ["cogs.seiyuu"]

bot = commands.Bot(command_prefix=">", owner_ID = 108430179084296192)

akane = 0

@bot.event
async def on_ready():
    print("Bot Ready")

@bot.command(name = "fools")
@commands.is_owner()
async def takeover(ctx):
    for mem in ctx.guild.members:
        print("id={}, nick={}".format(mem.id, mem.display_name))

@bot.command(name = "ping")
async def ping(self, ctx):
    await ctx.send("Pong")

@bot.command()
@commands.is_owner()
async def load(ctx, extension_name : str):
    """Loads an extension."""
    try:
        bot.load_extension(extension_name)
    except (AttributeError, ImportError) as e:
        await ctx.send("```py\n{}: {}\n```".format(type(e).__name__, str(e)))
        return
    await ctx.send("{} loaded.".format(extension_name))

@bot.command()
@commands.is_owner()
async def unload(ctx, extension_name : str):
    """Unloads an extension."""
    bot.unload_extension(extension_name)
    await ctx.send("{} unloaded.".format(extension_name))

@bot.command()
async def akanecounter(ctx,):
    await ctx.send("Akane-chan has been mentioned " + str(akane) + " times today!")


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if "akane" in message.content.lower():
        global akane
        akane += 1

    await bot.process_commands(message)

if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(extension, exc))

bot.run(config.TOKEN)
