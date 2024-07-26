
# AI-Powered Twitch Chat Bot with Text-to-Speech

This application is a Twitch chat bot that uses AI to generate responses to user commands and converts those responses to speech. It combines Twitch integration, AI text generation, and text-to-speech functionality to create an interactive experience for Twitch streamers and their audience.

## Features

- Responds to custom Twitch chat commands
- Generates AI responses using the Ollama library
- Converts AI responses to speech using text-to-speech technology
- Handles Unicode characters and special symbols in text-to-speech conversion
- Allows for easy customization of AI model and voice settings
- Everything runs locally on you PC

## Prerequisites

- Python 3.7 or higher
- A Twitch account and twitch developer access token
- Ollama installed on your system (for AI text generation)



## Installation

1. Clone this repository or download the source code.

2. Install the required Python packages:

   ```
   pip install twitchio ollama pyttsx3 keyboard
   ```
  I recommend installing them using pip separately.

3. Install Ollama by following the instructions at [ollama.com](https://ollama.com).

## Configuration

1. Open the script and replace the following placeholders:
   - `YOUR_TWITCH_ACCESS_TOKEN`: Your Twitch access token
   - `#TWITCH_USERNAME`: Your Twitch channel name

2. (Optional) Customize the AI model by changing the `model` parameter in the `AIHandler` class.

3. (Optional) Adjust the text-to-speech settings in the `AudioHandler` class:
   - Change the speech rate by modifying the `rate` property
   - Select a different voice by changing the voice index

## Usage

1. Run the script:

   ```
   python app.py
   ```

2. The bot will connect to your Twitch channel and listen for commands.

3. In your Twitch chat, use the command `!elai` followed by your message to interact with the AI:

   ```
   !elai Tell me a joke about programming
   ```

4. The bot will generate an AI response, send it to the Twitch chat, and speak it out loud.

5. To exit the program, press Ctrl+Q.

## How It Works

1. The application uses the `twitchio` library to connect to Twitch and listen for chat messages.

2. When a user sends a message starting with `!elai`, the bot processes it as a command.

3. The AI handler uses the Ollama library to generate a response based on the user's input.

4. The generated response is sent back to the Twitch chat.

5. Simultaneously, the audio handler converts the AI response to speech using the `pyttsx3` library.

6. The text-to-speech conversion runs asynchronously to avoid blocking the main bot operations.

## Customization

- You can change the command trigger (`!elai`) to any prefix you prefer.
- Modify the AI model or prompt in the `AIHandler` class to customize the AI responses.
- Adjust the text-to-speech settings in the `AudioHandler` class to change the voice or speech rate.

## Troubleshooting

- If you encounter issues with Ollama, make sure it's properly installed and the desired model is available.
- For text-to-speech problems, check that you have the necessary system libraries installed for `pyttsx3`.


## Acknowledgements

This project uses the following open-source libraries:
- TwitchIO
- Ollama
- pyttsx3
- keyboard


