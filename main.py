import discord
import os
import keep_alive
import pytz
import datetime
from discord.ext import tasks, commands

prefix = '$'
bot = commands.Bot(command_prefix=prefix)
s_hours = [7, 8, 9, 10, 11, 12, 13, 14]
s_days = [0, 1, 2, 3, 4]
channelid = 1111111111111111111

intents = discord.Intents.default()
intents.members = True


@tasks.loop(seconds=1)  # updates time every second
async def time_count():
    global now
    now = datetime.datetime.now(tz=pytz.timezone('America/New_York'))
    global hours
    hours = now.hour
    global minutes
    minutes = now.minute
    global currentday
    currentday = now.weekday()


@tasks.loop(seconds=60)  # alarm 2 minutes before each class starts from mon-fri
async def alarm():  # deletes them after 10 seconds
    if currentday in s_days:
        if minutes == 13:
            if hours in s_hours:
                await bot.wait_until_ready()
                channel = bot.get_channel(
                    channelid)  # gets channel id
                if hours == 7:
                    await channel.send('<@&796803092813053983>' +
                                       " 1st period is starting soon!",
                                       delete_after=120)
                elif hours == 8:
                    await channel.send('<@&796803092813053983>' +
                                       " 2nd period is starting soon!",
                                       delete_after=120)
                elif hours == 9:
                    await channel.send('<@&796803092813053983>' +
                                       " 3rd period is starting soon!",
                                       delete_after=120)
                elif hours == 10:
                    await channel.send('<@&796803092813053983>' +
                                       " 4th period is starting soon!",
                                       delete_after=120)
                elif hours == 11:
                    await channel.send('<@&796803092813053983>' +
                                       " 5th period is starting soon!",
                                       delete_after=120)
                elif hours == 12:
                    await channel.send('<@&796803092813053983>' +
                                       " 6th period is starting soon!",
                                       delete_after=120)
                elif hours == 13:
                    await channel.send('<@&796803092813053983>' +
                                       " 7th period is starting soon!",
                                       delete_after=120)


@bot.event  # sets presence, and starts time as well as alarm
async def on_ready():
    print("Logged in as {0.user}".format(bot))
    time_count.start()
    alarm.start()
    await bot.change_presence(activity=discord.Activity(
        type=discord.ActivityType.watching, name="your every move"))


@bot.event  # $time command
async def on_message(message):
    if message.content == (prefix + 'time'):
        if hours > 12:
            if 0 < minutes <= 9:
                await message.channel.send('It is currently ' +
                                           str(hours - 12) + ':' + '0' +
                                           str(minutes) + ' PM EST.')
            elif minutes > 10:
                await message.channel.send('It is currently ' +
                                           str(hours - 12) + ':' +
                                           str(minutes) + ' PM EST.')
        elif hours == 0:
            if 0 < minutes <= 9:
                await message.channel.send('It is currently ' + '12' + ':' +
                                           '0' + str(minutes) + ' PM EST.')

            elif minutes > 10:
                await message.channel.send('It is currently ' + '12' + ':' +
                                           str(minutes) + ' PM EST.')
        elif hours <= 12:
            if 0 < minutes <= 9:
                await message.channel.send('It is currently ' + str(hours) +
                                           ':' + '0' + str(minutes) +
                                           ' AM EST.')
            elif minutes > 10:
                await message.channel.send('It is currently ' + str(hours) +
                                           ':' + str(minutes) + ' AM EST.')


keep_alive.keep_alive()
bot.run(bot.run(os.getenv('TOKEN')))
