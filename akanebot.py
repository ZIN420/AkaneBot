import discord
from discord.ext import commands
from collections import defaultdict
import os
import random

import config
#
# startup_extensions = ["cogs.seiyuu"]

bot = commands.Bot(command_prefix=">", owner_ID = 108430179084296192)

akane = 0
usercounter = defaultdict(int)

@bot.event
async def on_ready():
    print("Bot Ready")

@bot.command(name = "takeover", description="Takesover the goddamn server")
@commands.is_owner()
async def takeover(ctx):

    ##Save current nicknames to revert them back afterwards
    save = open(str(ctx.guild) + '-servermemnicks.txt', 'wb')
    for mem in ctx.guild.members:
        out = "id={}, nick={}".format(mem.id, mem.display_name) + "\n"
        save.write(out.encode('utf_8'))
    print("Member nicks saved")

    ##Save current role colors to revert them back afterwards
    save = open(str(ctx.guild) + 'rolecolors.txt', 'w')
    for role in ctx.guild.roles:
        save.write("Role: " + str(role.name) + str(role.color) + "\n")
        print(role.permissions.change_nickname)
        for x in iter(role.permissions):
            print(x)
    print("Role colors saved")

    ##Set all nicknames to Pretty Nyannyan
    for mem in ctx.guild.members:
        try:
            await mem.edit(nick="Pretty Nyannyan -" + str(mem.name), reason="茜ちゃんだ☆！！")
        except Exception as e:
            pass
    print("Nyannyan Army Built")

    ##Change all Role Colors to Akane orange and change_nickname permission to False
    for role in ctx.guild.roles:
        print(role.permissions.change_nickname)
        try:
            perm = role.permissions
            perm.update(change_nickname = False)
            await role.edit(color=discord.Colour.from_rgb(235, 97, 63),permissions=perm)
            # print(role.permissions.change_nickname)
        except Exception as e:
            print(e)
            pass
    print("Nyannyan's brainwashed.")

    for x in ctx.guild.channels:
        try:

            await x.send("Akane-chan has taken over the server! Follow me pretty nyanyans!")
            imgList = os.listdir("./akane") # Creates a list of filenames from your folder

            imgString = random.choice(imgList) # Selects a random element from the list

            path = "./akane/" + imgString # Creates a string for the path to the file

            # await client.send_file(message.channel, path) # Sends the image in the channel the command was used
            await x.send(file=discord.File(path, filename="Akane-chan's cuteness.png"))
        except Exception as e:
            pass


@bot.command(name = "ping")
async def ping(ctx):
    await ctx.send("Pong")

# @bot.command()
# @commands.is_owner()
# async def load(ctx, extension_name : str):
#     """Loads an extension."""
#     try:
#         bot.load_extension(extension_name)
#     except (AttributeError, ImportError) as e:
#         await ctx.send("```py\n{}: {}\n```".format(type(e).__name__, str(e)))
#         return
#     await ctx.send("{} loaded.".format(extension_name))
#
# @bot.command()
# @commands.is_owner()
# async def unload(ctx, extension_name : str):
#     """Unloads an extension."""
#     bot.unload_extension(extension_name)
#     await ctx.send("{} unloaded.".format(extension_name))

@bot.command()
async def counter(ctx):
    await ctx.send("Akane-chan has been mentioned " + str(akane) + " times today!")
    await ctx.send("Akane-chan's Top Nyannyan's:")
    print(usercounter)
    result = ""
    for m in usercounter:
        result += (str(m) + ": " + str(usercounter[m]) + "\n")
    await ctx.send(result)


    await ctx.send("Have some more of Akane-chan's cuteness!")
    imgList = os.listdir("./akane") # Creates a list of filenames from your folder

    imgString = random.choice(imgList) # Selects a random element from the list

    path = "./akane/" + imgString # Creates a string for the path to the file

    # await client.send_file(message.channel, path) # Sends the image in the channel the command was used
    await ctx.send(file=discord.File(path, filename="Akane-chan's cuteness.png"))


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if "akane" in message.content.lower():
        global akane
        akane += 1
        global usercounter
        usercounter[message.author] += 1

    if "cute" in message.content.lower():
        await message.channel.send("Did someone say cute? Akane-chan is the cutest in the world!")
        imgList = os.listdir("./akane") # Creates a list of filenames from your folder

        imgString = random.choice(imgList) # Selects a random element from the list

        path = "./akane/" + imgString # Creates a string for the path to the file

        # await client.send_file(message.channel, path) # Sends the image in the channel the command was used
        await message.channel.send(file=discord.File(today))
        # await asyncio.sleep(10)


    await bot.process_commands(message)
#
# if __name__ == "__main__":
#     for extension in startup_extensions:
#         try:
#             bot.load_extension(extension)
#         except Exception as e:
#             exc = '{}: {}'.format(type(e).__name__, e)
#             print('Failed to load extension {}\n{}'.format(extension, exc))
#
bot.run(config.TOKEN)
