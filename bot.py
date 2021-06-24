# bot.py
import os

import discord
import pogInterface
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv('discord.env')
TOKEN = os.getenv('DISCORD_TOKEN')
Interactor = pogInterface.Sheet()


bot = commands.Bot(command_prefix='!')
@bot.command(name = "get")
async def get_pogs(ctx):
    currentString = "Toxic Tuesday Leaderboad: \n "
    await ctx.send(currentString)
    one_word_per_line = Interactor.printToxic()
    quote_text = '\n>>> {}'.format(one_word_per_line)
    await ctx.send(quote_text)
    currentString = "Wholesome Wednesday Leaderboad: \n "
    await ctx.send(currentString)
    one_word_per_line = Interactor.printWholesome()
    quote_text = '\n>>> {}'.format(one_word_per_line)
    await ctx.send(quote_text)


#TODO: Require the input be of type @username
@bot.command(name = 'ww')
async def update_wholesome(ctx, user_to_vote_for: str):
    completed = Interactor.updateWholesome(user_to_vote_for)
    currentString = "Wholesome Wednesday Leaderboad: \n "
    await ctx.send(currentString)
    one_word_per_line = Interactor.printWholesome()
    quote_text = '\n>>> {}'.format(one_word_per_line)
    await ctx.send(quote_text)


@bot.command(name='tt')
async def update_toxic_tuesday(ctx, user_to_vote_for : str): 
    completed = Interactor.updateToxic(user_to_vote_for)
    currentString = "Toxic Tuesday Leaderboad: \n "
    await ctx.send(currentString)
    one_word_per_line = Interactor.printToxic()
    quote_text = '\n>>> {}'.format(one_word_per_line)
    await ctx.send(quote_text)




@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CheckFailure):
        await ctx.send('You do not have the correct role for this command.')
bot.run(TOKEN)