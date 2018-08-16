import discord
from discord.ext import commands

from fuzzywuzzy import fuzz
from fuzzywuzzy import process

f = open("names.txt",'r')
file = f.readlines()

choices = []
for x in file:
    choices.append(x.strip("\n"))

class SeiyuuSearch():

    def __init__(self, bot):
        self.bot = bot
    # 
    # @commands.command(name = "ping")
    # async def ping(self, ctx):
    #     await ctx.send("Pong")

    @commands.command(name = "seiyuu", description = "search for a seiyuu")
    async def seiyuu(self, ctx, *, msg: str = None):
        x, result, arr = findSeiyuu(msg)
        if x:
            await ctx.send(result)
        else:
            await ctx.send(result)
            await ctx.send("Please select one of the above options by number.")

            def check(m):
                return m.channel == ctx.channel and m.author == ctx.author

            rep = await self.bot.wait_for('message', check = check)
            try:
                await ctx.send(arr[int(rep.content)])
            except Exception as e:
                await ctx.send("Invalid Option")


def setup(bot):
    bot.add_cog(SeiyuuSearch(bot))

def findSeiyuu(query):
    a=[]
    b=[]
    c=[]

    for x in process.extract(query, choices, scorer=fuzz.token_set_ratio, limit = 10):
        b.append(x)

    for x in process.extract(query, choices, limit = 10):
        c.append(x)

    matched = {} # Holds all returned results

    for x, match in enumerate(b,1): # Matches results that contain the entire query
        #print(match[1])
        if match[1] == 100:
            matched.update({x:match[0]})
            #print(match[0])

    exact = len(matched) # Number of results that contain entire query. Also index of the split.

    counter = exact+1 # Counter shifted for index

    for match in (c): # Results of all matches minus the ones that contain the entire query.
        if match[1] >= 90:
            if not match[0] in matched.values():
                matched.update({counter:match[0]})
                counter += 1

    result = "" # Return string

    if exact == 1: # If there is only one result that contains the entire query, return it and finish.
        m = matched[1]
        i = m.lower().find(query)
        result = (m[:i] + "**" + m[i:i+len(query)] + "**" + m[i+len(query):] + "\n") # Bolds the query in the result
        return (True, result, matched)

    elif exact >1:
        result = "Possible matches found:\n"
        for x in range(1,exact+1):
            m = matched[x]
            i = m.lower().find(query)
            result += (str(x) + ": " + m[:i] + "**" + m[i:i+len(query)] + "**" + m[i+len(query):] + "\n") # Bolds the query in the result

    if len(matched) > exact:
        if exact == 0:
            result += "No matches found. \n"
        result += "Maybe you meant:\n"
        for x in range(exact+1, len(matched)+1):
            m = matched[x]
            i = m.lower().find(query)
            result += (str(x) + ": " + m[:i] + "**" + m[i:i+len(query)] + "**" + m[i+len(query):] + "\n") # Bolds the query in the result

    if result == "":
        result += ("Sorry, I couldn't find **" + query + "**. Please try another query.")
        return (True, result, matched)


    return (False, result, matched)
