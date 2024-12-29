import discord
from ELIZA import ElizaBot
from dotenv import load_dotenv
import os

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')

# Initialize the ELIZA bot
eliza = ElizaBot()

intents = discord.Intents.default()
intents.message_content = True  # Make sure the bot can read messages

# Create a client instance of Discord bot with the correct intents
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    # Ignore messages from the bot itself
    if message.author == client.user:
        return
    
    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

    # Respond to the user's message
    response = eliza.respond(message.content)
    await message.channel.send(response)

# Replace 'YOUR_TOKEN_HERE' with your bot token
client.run(TOKEN)
