import os
import bot_commands
from discord.ext import commands

bot = commands.Bot(command_prefix='$')


@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send('Hello, how can I help you destroy your enemies?')
    await bot.process_commands(message)


@bot.command(pass_context=True)
async def mmr(ctx, name):
    await ctx.send(bot_commands.get_dota_mmr(name))


@bot.command(pass_context=True)
async def record(ctx, name):
    await ctx.send(bot_commands.get_win_loss_record(name))


@bot.command(pass_context=True)
async def averages(ctx, name):
    await ctx.send(bot_commands.get_player_averages(name))


@bot.command()
async def commands(ctx):
    await ctx.send('Available Commands: \n'
                   'mmr + [name] = Estimated Unranked MMR\n'
                   'record + [name] = Win/Loss Totals\n'
                   'averages + [name] = Performance Averages(Last 5 Games)')


bot.run('ODEzODQwNjYxNzQ3ODU5NDY2.YDVKLg.dKSA_Mj8bO_9Zj7CQjKPvL5zx3M')
