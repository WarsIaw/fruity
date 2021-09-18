import json
import os
import discord
from discord.ext import commands

if os.path.exists(os.getcwd() + "/config.json"):
    with open("./config.json") as f:
        configData = json.load(f)
else:
    config = {"Token": "", "Prefix": "!"}

    with open(os.getcwd() + "/config.json", "w") as f:
        json.dump(config, f)

token = configData["Token"]
prefix = configData["Prefix"]

bot = commands.Bot(command_prefix="prefix")

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))

bot.run(token)