import discord
from discord.ext import commands
import asyncio
import time

token = 'YOUR TOKEN HERE'
client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print('Pomodoro Discord Bot is ready.')

@client.command(pass_context=True)
async def logout(ctx):
    await client.logout()
    
@client.command(pass_context=True)
async def timer(ctx, *args):
    smallBreaks = 1
    workTime = 25 * 60
    smallBreakTime = 5 * 60 
    longBreakTime = 30 * 60
    if isinstance(int(args[0]), int) and isinstance(int(args[1]), int) and isinstance(int(args[2]), int):
        workTime = int(args[0]) * 60
        smallBreakTime = int(args[1]) * 60
        longBreakTime = int(args[2]) * 60
        while True:
            t = time.time()
            await ctx.send(f"{smallBreaks}/4 work cycles in progress. Next break at {time.strftime('%I:%M:%S %p', time.localtime(t + workTime))}.")
            if smallBreaks != 4:
                smallBreaks += 1
                time.sleep(workTime)
                await ctx.send(f"Small break! Start working at {time.strftime('%I:%M:%S %p', time.localtime(t + workTime + smallBreakTime))}.")
                time.sleep(smallBreakTime)
            else:
                smallBreaks = 0
                time.sleep(workTime)   
                await ctx.send(f"Long break! Start working at {time.strftime('%I:%M:%S %p', time.localtime(t + workTime + longBreakTime))}.")
                time.sleep(longBreakTime)
    else:
        await ctx.send("Arguments not given. Using default parameters.")

if __name__ == "__main__":
    client.run(token)