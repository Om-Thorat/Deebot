import os
import random
from googlesearch import search

import discord
from dotenv import DISCORD_TOKEN,DISCORD_GUILD

TOKEN = DISCORD_TOKEN
GUILD = DISCORD_GUILD
client = discord.Client()

@client.event
async def on_ready():
    guild = discord.utils.get(client.guilds,name=GUILD)
    print(f'{client.user} has connected to Discord!')
    print(f'{guild.name}(id: {guild.id})')
    members = '\n - '.join([member.name for member in guild.members])
    print(f'Some Humans:\n - {members}')
h=1
loose = 0
win = 0
draw = 0
i=1
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    global i
    global h,loose,win,draw
    if message.content.startswith ("spam"):
        f=open("Discordmsgs.txt","a")
        f.write("\n")
        f.write(message.content)
        x=message.content[7:]
        y=(message.content[4:7])
        while i <= int(y):
                    await message.channel.send(x)
                    i=i+1
                    print(i)
    elif "stop" in message.content.lower():
        i=100
        print(i)
    elif "resume" in message.content.lower():
        i=1
    elif message.content.startswith ("!g"):
            user=(message.content[3:])
            print(user)
            Options=["Snake","Water","Gun"]
            a=random.choice(Options)
            if a == "Snake" and user =="Water":
                await message.channel.send(a)
                await message.channel.send ("loose")
                loose = loose + 1
            elif a == user :
                await message.channel.send(a)
                await message.channel.send("Tie")
                draw = draw + 1
            elif a == "Snake" and user == "Gun":
                await message.channel.send(a)
                await message.channel.send("win")
                win = win +1
            elif a == "Water" and user == "Gun":
                await message.channel.send(a)
                await message.channel.send("loose")
                loose = loose + 1
            elif a == "Water" and user == "Snake":
                await message.channel.send(a)
                await message.channel.send("win")
                win = win + 1
            elif a == "Gun" and  user == "Snake":
                await message.channel.send(a)
                await message.channel.send("loose")
                loose = loose +1
            elif a == "Gun" and user == "Water":
                await message.channel.send(a)
                await message.channel.send("win")
                win = win + 1
            else:
                await message.channel.send("please choose between Snake,Water,Gun Only,Game closed use !g to restart")
    elif "endgame" in message.content.lower():
        f="you won"+" "+str(win)+" "+"times"
        g="you lost"+" "+str(loose)+" "+"times"
        dd="you drew"+" "+str(draw)+" "+"times"    
        await message.channel.send(f)
        await message.channel.send(g)
        await message.channel.send(dd)
        if win >> loose:
            await message.channel.send("yay you won")
        elif loose >> win:
           await message.channel.send("Oh you lost :(")
        else:
            await message.channel.send("it's a draw")
    elif "bothelp" in message.content.lower():
                                   await message.channel.send("To spam send Spam**number of times** **the thing to spam**")
                                   await message.channel.send("send stop to stop spam feature")
                                   await message.channel.send("send resume to restart the spam feature")
                                   await message.channel.send("To play snake water gun send !g **your choice**")
    elif message.content.startswith ("hey dee"):
        query=(message.content[8:])
        for x in search(query, tld="co.in", num=1, stop=1, pause=2): 
            await message.channel.send(x)
    elif message.content.startswith ("good bot"):
        await message.channel.send("Thank you : )")
    else:
        f=open("Discordmsgs.txt","a")
        f.write("\n")
        f.write(message.content)
        print(message.content)
        

client.run(TOKEN)
