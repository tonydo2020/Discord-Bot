import discord
import os
from discord.ext import commands


client = commands.Bot(command_prefix ="") #Looking for commands
    
@client.event
async def on_ready():
    print("Bot is ready!")


@client.event
async def on_message(message):
    messages = message.content
    words = messages.split()
    print(words)
    filename = 'read_messages.txt'
    if os.path.exists(filename):
        append_write ='a'
    else:
        append_write ='w'


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
client.run('NjIzNjc5NjcyNTMzOTA5NTE1.XYMSkg.pWEcJUBIw_h4xsNLLLYdsDB-8ZM')
