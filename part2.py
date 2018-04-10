import discord
from discord.ext import commands
from collections import defaultdict
import os
import random

import config
#
# startup_extensions = ["cogs.seiyuu"]

bot = commands.Bot(command_prefix=">", owner_ID = 108430179084296192)


colors = {'AkaneP':0xeb613f,'AmiP':0xffe43f,'AnnaP':0x7e6ca8,'ArisaP':0xb54461,'AyumuP':0xe25a9b,'AzusaP':0x2743d3,'ChihayaP':0x2743d2,'ChizuruP':0xf19557,'ElenaP':0x9bce92,'EmilyP':0x554171,'FukaP':0x7278a8,'HarukaP':0xe12b31,'HibikiP':0x01adb9,'HinataP':0xd1342c,'IkuP':0xf7e78e,'IoriP':0xfd99e1,'Julia':0xd7385f,'KanaP':0xf5ad3b,'KaoriP':0x152b65,'KarenP':0xb63b40,'KonomiP':0xf1becb,'KotohaP':0x92cfbb,'MakotoP':0x515558,'MamiP':0xffe43f,'MatsuriP':0x5abfb7,'MegumiP':0x454341,'MikiP':0xb4e04b,'MinakoP':0x58a6dc,'MiraiP':0xea5b76,'MiyaP':0xd7a96b,'MizukiP':0x99b7dc,'MomokoP':0xefb864,'NaoP':0x788bc5,'NorikoP':0xeceb70,'ReikaP':0x6bb6b0,'RioP':0xf19591,'RitsukoP':0xe12b32,'RocoP':0xfff03c,'SayokoP':0x7f6575,'SerikaP':0xed90ba,'ShihoP':0xafa690,'ShizukaP':0x6495cf,'SubaruP':0xaeb49c,'TakaneP':0xa6126a,'TamakiP':0xee762e,'TomokaP':0xbee3e3,'TsubasaP':0xfed552,'TsumugiP':0xb5b1e1,'UmiP':0xe9739b,'YayoiP':0xf39939,'YukihoP':0xd3dde9,'YurikoP':0xc7b83c}
akane = 0
usercounter = defaultdict(int)

@bot.event
async def on_ready():
    print("Bot Ready")

@bot.command(name = "revert", description="Everything goes back to normal")
@commands.is_owner()
async def revert(ctx):

    # Save current nicknames to revert them back afterwards
    # save = open(str(ctx.guild) + '-servermemnicks.txt', 'wb')
    # for mem in ctx.guild.members:
    #     out = "id={}, nick={}".format(mem.id, mem.display_name) + "\n"
    #     save.write(out.encode('utf_8'))
    # print("Member nicks saved")

    ##Save current role colors to revert them back afterwards
    # save = open(str(ctx.guild) + 'rolecolors.txt', 'w')
    # for role in ctx.guild.roles:
    #     save.write("Role: " + str(role.name) + str(role.color) + "\n")
    #     print(role.permissions.change_nickname)
    #     for x in iter(role.permissions):
    #         print(x)
    # print("Role colors saved")

    ##Reverts all nicknames
    for mem in ctx.guild.members:
        try:
            await mem.edit(nick=mem.name, reason="Reversion")
        except Exception as e:
            pass
    print("Names Reverted")

    ##Change all Role Colors to back to normal and fix nickname permissions
    for role in ctx.guild.roles:
        #print(role.permissions.change_nickname)
        try:
            current = role.name
            perm = role.permissions
            perm.update(change_nickname = True)
            await role.edit(color=discord.Colour(colors[current]),permissions=perm)
            # print(role.permissions.change_nickname)
        except Exception as e:
            #print(e)
            pass
    print("Nyannyan's reverted to boring people.")

    for x in ctx.guild.channels:
        try:

            await x.send("Thanks for playing with Akane-chan today! It was lots of fun! ")

            await x.send("Akane was mentioned by name 277 times todaya and my top Pretty Nyannyan was kiryuna with 33 mentions!")
            imgList = os.listdir("./akane") # Creates a list of filenames from your folder

            # imgString = random.choice(imgList) # Selects a random element from the list

            path = "birthday.gif"  # Creates a string for the path to the file

            # await client.send_file(message.channel, path) # Sends the image in the channel the command was used
            await x.send(file=discord.File(path, filename="ThankYou.gif"))
            await x.send("If you want to see more of Akane-chan's cuteness for the rest of the day, just call me with >cute at anytime!")
        except Exception as e:
            pass


# @bot.command(name = "ping")
# async def ping(ctx):
#     await ctx.send("Pong")

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

# @bot.command()
# async def counter(ctx):
    await ctx.send("Akane-chan has been mentioned " + str(akane) + " times today!")
    await ctx.send("Akane-chan's Top Nyannyan's:")
    print(usercounter)
    result = ""
    for m in usercounter:
        result += (str(m) + ": " + str(usercounter[m]) + "\n")
    await ctx.send(result)


    await ctx.send("Have some more of Akane-chan's cuteness!")
    imgList = os.listdir("./akane") # Creates a list of filenames from your folder

    # imgString = random.choice(imgList) # Selects a random element from the list

    path = "./akane/birthday.gif"  # Creates a string for the path to the file

    # await client.send_file(message.channel, path) # Sends the image in the channel the command was used
    await ctx.send(file=discord.File(path, filename="ThankYou.gif"))

@bot.command(name = "cute", description="PMs an Akane pic")
async def akanecute(ctx):

    imgList = os.listdir("./akane") # Creates a list of filenames from your folder

    imgString = random.choice(imgList) # Selects a random element from the list

    path = "./akane/" + imgString # Creates a string for the path to the file
    await ctx.author.send(content="Cute is Akane-chan! Have an Akane-chan pic.", file=discord.File(path, filename="ThankYou.png"))
    #await ctx.author.send("Pong")

# @bot.event
# async def akane_cute(message):
#     if message.author == bot.user:
#         return
#
#     if "akane" in message.content.lower():
#         # global akane
#         akane += 1
#         global usercounter
#         usercounter[message.author] += 1
#
#     if ("cute" in message.content.lower() and "akane" in message.content.lower()):
#
#         imgList = os.listdir("./akane") # Creates a list of filenames from your folder
#
#         imgString = random.choice(imgList) # Selects a random element from the list
#
#         path = "./akane/" + imgString # Creates a string for the path to the file
#         await message.author.send(content="Cute is Akane-chan! Have an Akane-chan pic.", file=discord.File(path, filename="ThankYou.png"))
#
#         # await client.send_file(message.channel, path) # Sends the image in the channel the command was used
#         # await message.author.send()
#         # await asyncio.sleep(10)


    # await bot.process_commands(message)
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
