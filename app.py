import asyncio
import twitchio
from twitchio.ext import commands
import ollama
import pyttsx3
import re
import unicodedata
import textwrap
import concurrent.futures
import keyboard  # Import the keyboard module
import sys  # Import sys for exiting the program
import os  # Import os for closing the terminal

class AIHandler:
    @staticmethod
    async def generate_response(prompt):
        try:
            # you can change the model to your prefered model from the ollama.com library
            response = ollama.chat(model='llama3.1', messages=[
                {'role': 'user', 'content': prompt},
            ])
            return response['message']['content']
        except Exception as e:
            print(f"Error generating AI response: {e}")
            return "I'm sorry, I couldn't generate a response at this time."

class AudioHandler:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 150)  # Speed of speech
        self.executor = concurrent.futures.ThreadPoolExecutor(max_workers=1)
        voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', voices[0].id)  # Use the first available voice

    def clean_text(self, text):
        text = unicodedata.normalize('NFKD', text).encode('ASCII', 'ignore').decode('ASCII')
        text = re.sub(r'[^a-zA-Z0-9\s.,!?-]', '', text)
        return text

    def text_to_speech(self, text):
        cleaned_text = self.clean_text(text)
        self.engine.say(cleaned_text)
        self.engine.runAndWait()

    async def async_text_to_speech(self, text):
        await asyncio.get_running_loop().run_in_executor(self.executor, self.text_to_speech, text)

class TwitchBot(commands.Bot):
    def __init__(self):
        super().__init__(token='YOUR_TWITCH _ACCESS_TOKEN', prefix='!', initial_channels=['#TWITCH_USERNAME']) # Replace 'YOUR_TWITCH_USERNAME' with your Twitch username and 'YOUR_TWITCH_ACCESS_TOKEN' with your Twitch access token
        self.ai_handler = AIHandler()
        self.audio_handler = AudioHandler()

    async def event_ready(self):
        print(f'Logged in as | {self.nick}')

    async def event_message(self, message):
        if message.echo:
            return

        if message.content.strip().lower().startswith("!elai"): # you can change this  command name to whatever you want
            await self.handle_elai_command(message)

    async def handle_elai_command(self, message):
        content = message.content.strip()[5:].strip()
        if content:
            await self.process_elai_request(content, message.channel)
        else:
            await message.channel.send("Hello! Please provide a message after !elai.") # change the message here to include your command if you changed the command

    async def process_elai_request(self, content, channel):
        try:
            response = await self.ai_handler.generate_response(f"User asked: {content}")

            # Split the response into chunks of 500 characters or less
            response_chunks = textwrap.wrap(response, 495, replace_whitespace=False, break_long_words=True)

            # Generate the response as chunks of text and send it to the twitch chat as a message
            # for i, chunk in enumerate(response_chunks):
            #     prefix = f"Part {i+1}/{len(response_chunks)}: " if len(response_chunks) > 1 else ""
            #     await channel.send(f"{prefix}{chunk}")


            # Use the new async method for TTS
            await self.audio_handler.async_text_to_speech(response)

            await channel.send("Response generated and spoken.")
        except Exception as e:
            print(f"Error processing message: {e}")
            await channel.send("Sorry, there was an error processing your request.")

def main():
    bot = TwitchBot()
    loop = asyncio.get_event_loop()

    def on_exit():
        print("Ctrl + Q pressed. Exiting...")
        os._exit(0)  # Close the terminal immediately

    keyboard.add_hotkey('ctrl+q', on_exit)  # Register the hotkey

    try:
        loop.run_until_complete(bot.run())
    finally:
        loop.close()

if __name__ == "__main__":
    main()