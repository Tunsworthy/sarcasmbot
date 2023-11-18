import os
import openai
import discord
import requests
from requests.exceptions import Timeout
from openai import OpenAI
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

bot_token = os.getenv('DISCORD_API_Key')
openai_api_key = os.getenv('OPENAI_API_KEY')

intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix='!', intents=intents)
openai = OpenAI(api_key=openai_api_key)


def is_joke_or_play_on_words(message_content, client_instance, model="gpt-4", timeout=10):
    messages = [{"role": "user", "content": "Does this message contain a joke, jokey tone,sarcasm, pun or play on words. If it doesn't reply no, if it does reply yes with a reason seperated by a ," + message_content}]
    
    try:
        response = client_instance.chat.completions.create(
            model=model,
            messages=messages,
            temperature=0,
        )

        if response.choices and response.choices[0].message:
            print (response.choices[0].message)
            classification_result = response.choices[0].message.content.split(",")[0]
            if classification_result.lower() == 'yes':
                return True
            return False
        else:
            print("Error: Unexpected response format from OpenAI API")
            return False
    except Timeout:
        print("Error: OpenAI API request timed out")
        return False

    except Exception as e:
        print(f"Error calling OpenAI API: {e}")
        return False

def generate_sarcastic_response(message_content, client_instance, model="gpt-4", timeout=10):
    messages = [{"role": "user", "content": "Please reply to this message as a character form archer, no need to say who ," + message_content}]
    
    try:
        response = client_instance.chat.completions.create(
            model=model,
            messages=messages,
            temperature=0,
        )

        if response.choices and response.choices[0].message:
            print (response.choices[0].message)
            return response.choices[0].message.content
        else:
            print("Error: Unexpected response format from OpenAI API")
            return False
    except Timeout:
        print("Error: OpenAI API request timed out")
        return False

    except Exception as e:
        print(f"Error calling OpenAI API: {e}")
        return False

@client.event
async def on_ready():
    print(f'Logged in as {client.user.name}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    #print (message)
    print (f"Message: {message.content} User: {message.author}")
    if is_joke_or_play_on_words(message.content, openai):
        try:
            sarcastic_response = generate_sarcastic_response(message.content, openai)
            await message.channel.send(sarcastic_response)
        except Exception as e:
            print(f"Error: {e}")

    await client.process_commands(message)

# Replace "YOUR_DISCORD_BOT_TOKEN" with your actual Discord bot token
client.run(bot_token)