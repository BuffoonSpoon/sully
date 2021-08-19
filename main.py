# IMPORT DISCORD.PY. ALLOWS ACCESS TO DISCORD'S API.
import discord

# IMPORT THE OS MODULE.
import os

# IMPORT LOAD_DOTENV FUNCTION FROM DOTENV MODULE.
from dotenv import load_dotenv

# IMPORT COMMANDS FROM THE DISCORD.EXT MODULE.
from discord.ext import commands

# LOADS THE .ENV FILE THAT RESIDES ON THE SAME LEVEL AS THE SCRIPT.
load_dotenv()

# GRAB THE API TOKEN FROM THE .ENV FILE.
TOKEN = os.getenv("TOKEN")

print('Bot online!')

# CREATES A NEW BOT OBJECT WITH A SPECIFIED PREFIX. IT CAN BE WHATEVER YOU WANT IT TO BE.
bot = commands.Bot(command_prefix="!")


@bot.command(
  help="!say <message>",
	brief=" -- Says your message back to you!"
)
async def say(ctx, *args):
	response = ""

	for arg in args:
		response = response + " " + arg

	await ctx.channel.send(response)

@bot.command(
  help="!ping",
	brief=" -- Uses an incredibly complex method to ping your signal"

)
async def ping(ctx):
	await ctx.channel.send("pong")

@bot.command(
  help="!youtube",
	brief=" -- Sends Sully's Youtube Channel"

)
async def youtube(ctx):
  await ctx.channel.send("**Sully's Youtube Channel:** https://www.youtube.com/channel/UCqaS6ZnbGMcF_hqkzqr247Q/")

# EXECUTES THE BOT WITH THE SPECIFIED TOKEN. TOKEN HAS BEEN REMOVED AND USED JUST AS AN EXAMPLE.
bot.run(TOKEN)
