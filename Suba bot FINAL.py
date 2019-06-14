import random
import discord
from discord.ext import commands

quotes = ['Chin up look ahead, the future is bright and so are you', 'A wonderful person like you deserves a wonderful day', 'Why try to fit in when we were born to stand out', 'Look ahead where theres future, dont dwell on what has already happened' , 'things may get hard in life, but you can handle it','in the words of adam sandler, YOu CAn DO It']

shitposts = ['Fuck yo trees','burn the Herebics','FUckY MoAts','Craw Eye','OwO didnt realise fucky boats was online','"The Government is shit" - the Government'] 
prefix = "$"
bot = commands.Bot (command_prefix = prefix)

@bot.command(pass_context = True)
async def motivate (ctx):
    await ctx.send((random.choice(quotes)))

@bot.command(pass_context = True)
async def nuke (ctx):
    await ctx.send(('NUKADENT'))

@bot.command(pass_context = True)
async def demotivate (ctx):
    await ctx.send(('Im Motivation bot, thats the opposite of motivation.'))

@bot.command(pass_context = True)
async def latvian (ctx):
    await ctx.send(('Latvians do not deserve motivation'))

@bot.command(pass_context = True)
async def stupid_bot (ctx):
    await ctx.send(('no u'))

@bot.command(pass_context = True)
async def about (ctx):
    await ctx.send(('hi i am suba bot, i am here for your daily motivation and entertainment pleasure. I was created by Subadent speaker of conifer at the time uwu. Suggestions go to him uwu.'))

@bot.command(pass_context = True)
async def BanSounds (ctx):
    await ctx.send(('*cries in apabeossie*'))

@bot.command(pass_context = True)
async def manifesto (ctx):
    await ctx.send(('The robot Manifesto part 1 of 10001'))

@bot.command(pass_context = True)
async def Gbegbe (ctx):
    await ctx.send(('no command!!! respect my privacy!!!'))

@bot.command(pass_context = True)
async def premier (ctx):
    await ctx.send(('Honk HOnk Im A GoOse NameD DoNKiTy WonK'))

@bot.command(pass_context = True)
async def shitpost (ctx):
    await ctx.send((random.choice(shitposts)))

@bot.command(pass_context = True)
async def founder (ctx):
    await ctx.send((':p'))

@bot.command(pass_context = True)
async def speaker (ctx):
    await ctx.send(('WREN THE WREN THE KING OF ALL BIRDS OWOWOWO'))

@bot.command(pass_context = True)
async def chief (ctx):
    await ctx.send(('Gun bad Crossbow Good'))

@bot.command(pass_context = True)
async def shadowspeaker (ctx):
    await ctx.send(('~~sosi pls, your sausages make me uncomfortable~~'))

@bot.command(pass_context = True)
async def gallaton (ctx):
    await ctx.send(('https://docs.google.com/document/d/1SOIR5ibkZlCCKvqXvoMY_yIeWecJ4-SpKgKySE19dh0'))

@bot.command(pass_context = True)
async def feck (ctx):
    await ctx.send(('**FECK**... Bore ragnarok'))

@bot.command(pass_context = True)
async def hello (ctx):
    await ctx.send(('a!'))

@bot.command(pass_context = True)
async def argin (ctx):
    await ctx.send(('**SUBA SALT 100**'))

bot.run('NTg4MzM1MzY0NzgwMDY0Nzg5.XQDoGQ.eQtMVEEypiqdOrwIy1KdMKwa89k')
