import discord
from discord.ext import commands

#System Modules
import os
import glob
import random
import json
import datetime
from collections import defaultdict

# Custom Modules
import plotp
import config # GSheets authentication
#
startup_extensions = ["cogs.helper"]

bot = commands.Bot(command_prefix=">", owner_ID = 108430179084296192)

# Functions

def reload_list():
    path = 'Discord Logging/' + today
    print(path)
    global spokenusers
    for filename in glob.glob(os.path.join(path, '*.txt')):

        with open(filename, 'r', encoding = 'utf-8') as f:
            d = f.read()

        out = "{" + d[:-1] + "}"



        dic = json.loads(out)
        print(dic)

        guild = os.path.basename(filename[:-4])
        print(guild)
        spokenusers[guild].update(dic)

        print(guild + " loaded successfully")
        print(spokenusers[guild])# Upon starting, attempt to reload any lists from today

usercounter = defaultdict(int) # For stuff
spokenusers = defaultdict(lambda: {}) # List of users who have spoken today {guild:{userid:username}}
rolecol = defaultdict(int) # Collection of P roles {guild:P}

today = str(datetime.date.today())
timelogger = defaultdict(lambda: defaultdict(int)) # {guild:{hour:counter}}

@bot.event
async def on_ready():
    reload_list()
    print("Bot Ready")

@bot.command(name = "heh")
@commands.is_owner()
async def heh(ctx):
    await ctx.message.delete()
    text = input("Enter text\n")
    while not text == "end":
        await ctx.send(text)
        text = input("Enter text\n")


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

@bot.command(name = 'usersbyp', description = 'display number of users in each P role')
async def userpie(ctx):
    rolecol = defaultdict(int)
    for mem in ctx.guild.members:
        print(str(mem.roles) + str(mem.name))
        try:
            for role in mem.roles[1:]:
                rolecol[role] += 1
        except Exception as e:
            print(e)
            pass
    print(rolecol)
    # stuff

    labels = []
    for x in rolecol:
        labels.append(x.name)
    print(labels)

    sizes = list(rolecol.values())
    print(sizes)

    colors=[]
    for r in rolecol:
            colors.append(str(r.color))
    #explode = (0, 0.1, 0, 0)
    print(colors)

    name = to_filename.clean_filename(str(ctx.guild))

    await ctx.send(file=discord.File(plotp.plotpie(sizes, labels, colors, name)))

@bot.event
async def on_message(message):

    global today

    if not today == str(datetime.date.today()):
        global spokenusers
        spokenusers = defaultdict(lambda: {})
        today = str(datetime.date.today())

    aut = message.author
    autid =str(message.author.id)
    autname = str(message.author.name)
    gid = str(message.guild.id)
    if message.author.bot:
        return

    print(spokenusers[gid])

    if autid not in spokenusers[gid]:
        spokenusers[gid].update({autid:autname})
        print(aut.name + " has been added to {}'s active list of {}.".format(message.guild, today)) # Console log

        # Create dir if it does not exist
        file_path = "Discord Logging/" + str(datetime.date.today()) + "/"
        directory = os.path.dirname(file_path)
        if not os.path.exists(directory):
            os.makedirs(directory)

        # Open file to log
        name = str(message.guild.id) # to_filename.clean_filename(str(message.guild))
        with open(file_path + name + ".txt", 'ab') as o:
            o.write (('"' + autid + '": "' + autname + '",').encode('utf_8'))
            #o.write(b", \n")

        global rolecol
        try:
            rolecol[aut.roles[1]] += 1
        except Exception as e:
            print(aut.display_name + " has no roles")
            pass

    global timelogger

    hour = '"' + str(datetime.datetime.now().strftime('%Y-%m-%d %H')) + '"'
    timelogger[gid][hour] += 1

    await bot.process_commands(message)

@bot.command()
async def save_time(ctx):
    ##Save Guild Time Log
    for x in spokenusers:
        file_path = "Discord Logging/" + str(datetime.date.today()) 	+ "/"
        with open(file_path + x + ".txt", 'w') as o:
            o.write(x + ': "' + spokenusers[x] + '",')
    await ctx.send("time saved")

if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(extension, exc))
# other stuff
bot.run(config.TOKEN)
