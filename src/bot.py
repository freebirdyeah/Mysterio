import discord, os, random
from discord.ext import commands
from llm import get_bot_reply
# from dotenv import load_dotenv

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    print(f"Mysterio is online as {bot.user}")


@bot.event
async def on_message(message):

    if bot.user in message.mentions:
        reply = get_bot_reply(f"{message.content} (A user is trying to talk to you, talk with them)")
        await message.channel.send(reply)
    
    else:
        await bot.process_commands(message)


@bot.command(name="8ball")
async def eight_ball(ctx):

    eight_ball_responses = [
    "Your luck is the kind ancient scrolls warned us about — tragically comedic.",
    "Even the gods are facepalming. You've managed to roll a cosmic zero.",
    "The stars murmur… 'not today, perhaps not ever'.",
    "A faint breeze says no. Or maybe it's just apathy on the wind.",
    "There's a shimmer of hope... unless that's just static.",
    "Possibility twitches — faint, fickle, but definitely there.",
    "The universe wills it",
    "A llama sneezed in Peru — you'll be lucky."
    ]

    
    response = random.choice(eight_ball_responses)
    
    # Logging the message in which the bot was mentioned
    print(ctx.message.content)
    
    await ctx.send(response)


@bot.command(name="prophecy")
async def prophecy(ctx):

    mentions = ctx.message.mentions 
    message = ctx.message.content

    if not mentions:
        await ctx.send("You must mention someone to read their fate, mortal.")
        return

    # logging the mentions
    print(mentions)

    # loop over the mentioned users
    for member in mentions:
        reply = get_bot_reply(f"{ctx.author} asked the fates about {member.display_name}")
        await ctx.send(f"🔮 {member.mention}: {reply}")


@bot.command(name="judge")
async def judge(ctx):
    mentions = ctx.message.mentions 
    message = ctx.message.content

    if not mentions:
        await ctx.send("You must mention someone to judge them, mortal.")
        return

    # logging the mentions
    print(mentions)

    # loop over the mentioned users
    for member in mentions:
        reply = get_bot_reply(f"{ctx.author} asked to judge {member.display_name}, CONTEXT: {message}")
        await ctx.send(f"⚖️ {member.mention}: {reply}")


@bot.command(name="wisdom")
async def wisdom(ctx):
    reply = get_bot_reply(f"{ctx.author} asked for some wisdom")
    await ctx.send(reply)


# load_dotenv(), FOR LOCAL ENVIRONMENT

TOKEN = os.getenv("DISCORD_TOKEN")
bot.run(token=TOKEN)