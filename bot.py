import discord
import random
import os

TOKEN = os.getenv("TOKEN")
intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
intents.message_content = True  # VERY important for reading message content

client = discord.Client(intents=intents)

message_bank = [
    "Meow! 😺",
    "Meowww! 🐾🐾",
    "Mewww! 😻",
    "MEoWWWwwzaa! 😼",
    "meow motherfuckers. 😽",
    "Meowdy 🤠",  
    "Meowgic ✨",  
    "Meow-nificent 😻",  
    "Meowch! 😾",  
    "Meow-sic to my ears 🎶",  
    "Meowvelous! 🐱",

]
@client.event
async def on_message(message):
    if message.author == client.user:
        return  # don't respond to yourself
    if any(x in message.channel.name for x in ["announcements", "osterpasswords", "dinner-cook"]):
        return
    if all(letter in message.content.lower() for letter in "meowvindaloo" and random.randint(0, 1) == 0):
        await message.channel.send(random.choice(message_bank))


client.run(TOKEN)