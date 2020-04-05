import discord
import sqlite3
from discord.ext import commands
from discord.ext.commands import Bot
from datetime import datetime

client = Bot(command_prefix = None)
client.remove_command("help")

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game(name="Filling out forms."))
    print("Application Manager 2000 activated at " + datetime.now().strftime("%H:%M:%S"))

@client.event
async def on_message(message):
    if str(message.channel) == "application-channel" and message.content[0:7].strip() == "!apply4":
        userContent = message.content[7:].replace(" ", "").lower()
        jobValue = 0
        if userContent == "inventor":
            jobValue = 1
        elif userContent == "bugcatcher":
            jobValue = 2
        elif userContent == "alienresearcher":
            jobValue = 3
        elif userContent == "help":
            await message.channel.send("```\nType in !apply4 before a job in order to apply. EG: !apply4 {JOBNAME}\n```\n```\nAVALIABLE JOBS:\nBug Catcher\nInventor\nAlien Researcher\n```")
            return
        else:
            await message.channel.send(message.author.mention + " No such job found!\n```\nAVALIABLE JOBS:\nBug Catcher\nInventor\nAlien Researcher\n```")
            return
        connection = sqlite3.connect("applyBot.db") 
        cursor = connection.cursor()
        cursor.execute("INSERT INTO applications (user, job) VALUES (" + str(message.author.id) + ", " + str(jobValue) + ");")
        connection.commit()
        await message.channel.send("Accepted " + message.author.mention + "'s request for " + userContent + "!")
        connection.close()

client.run("Njk2MDMyMTk2NDAxODIzODE2.Xoi0vQ.uUi1zJmFz5qzePXJBnKlVqu5Dos")