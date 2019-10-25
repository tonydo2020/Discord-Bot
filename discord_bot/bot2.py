import discord
import os
from discord.ext import commands
from datetime import date 

client = commands.Bot(command_prefix ="") #Looking for commands
    
@client.event
async def on_ready():
    print("Bot is ready!")
    


@client.event
async def on_message(message):
    messages = message.content
    words = messages.split()
    print(words)


    filename  = (today.strftime("%d_%m_%Y") + ".txt")
    
    if os.path.exists(filename):
        append_write ='a'
    else:
        append_write ='w'
        print(append_write)

    file = open(filename, append_write)
    
    for word in words:
        file.write(word + '\n')
    file.close()

    
    

##@client.event
##async def new_message(message):
##    filename = read_messages.txt
##    if os.path.exists(file):
##        append_write = 'a'
##    else:
##        append_write = 'w'
##
##
##    file = open(filename, append_write)
##    file.write(message + '\n')
##    file.close()
##    
##
##@client.command(pass_context=True)
##async def clear(ctx, amount=1):
##    channel = ctx.message.channel
##    messages = []
##    filename = read_messages.txt
##    if os.path.exists(file):
##        append_write ='a'
##    else:
##        append_write ='w'
##
##    file = open(filename, append_write)
##    async for message in client.logs_from(channel, limit=int(amount)):
##        messages.append(message)
##        file.write(message + '\n')
##        print(message)

        

##    file.close()
today = date.today()
client.run("Bot token goes here")
