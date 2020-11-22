import discord
import json
import asyncio

bot = discord.Client()

a = {}

@bot.event
async def on_ready():
    
    global a

    with open("/Users/test/Desktop/Discord Bots/Coding_Challenges/main.json", "r") as mjson:
        
        a = json.load(mjson)
        
        mjson.close()

    if len(a) == 0:
        
        a = {}

        for member in bot.get_guild("779290532622893057").members:
        
            a[str(member.id)] = {"xp" : 0, "messageCountdown" : 0}

    print("Ready...")

    while True:
        
        try:
            
            for member in bot.get_guild("779290532622893057").members:
            
                a[str(member.id)]["messageCountdown"] -= 1

        except:
            
            pass

        await asyncio.sleep(1)

@bot.event
async def on_message(message):
    
    global a

    if message.content == ":stop" and message.author.id == 779290532622893057:
        
        with open("main", "w") as mjson:
            
            mjson.write(json.dumps(a))
            mjson.close()
        
        await bot.close()

    elif message.content == ":xp":

        await message.channel.send(a[str(message.author.id)]["xp"])

    elif message.author != bot.user:

        if a[str(message.author.id)]["messageCountdown"] <= 0:
            
            a[str(message.author.id)]["xp"] += 15

            a[str(message.author.id)]["messageCountdown"] = 15


@bot.event
async def on_member_join(member):

    a[str(member.id)] = {"xp" : 0, "messageCountdown" : 0}

bot.run("Nzc5NDg5Njk1Njc0OTI1MDc2.X7hSWQ.oWod6_FZgfleHyCxxwVjYAPpMao")