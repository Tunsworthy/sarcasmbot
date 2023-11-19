# Discord Sarcastic Bot

The Discord Sarcastic Bot is a Python-based chatbot designed to operate on the Discord platform. Its primary function is to engage with users in a humorous and sarcastic manner, responding with witty and dry remarks when someone in the Discord server makes a joke, pun, play on words, or attempts to be funny.

## Features

- **Joke Classification:** The bot utilizes the OpenAI Chat API to classify incoming messages and determine whether they contain a joke, pun, play on words, or an attempt at humor.

- **Sarcastic Responses:** If a user's message is identified as humorous, the bot generates and delivers a sarcastic response, adding a touch of humor to the conversation.

- **Discord Integration:** The bot seamlessly integrates into Discord servers, monitoring messages and contributing to the playful atmosphere with its sarcastic replies.


## Prerequisites

- Python
- Docker
- Discord API key
- OpenAI API key

## Getting Started

1. Clone the repository:
   ```bash
   git clone https://github.com/Tunsworthy/sarcasmbot.git
   cd sarcasmbot
   ```

2. Build the Docker image:
   ```bash
   docker build -t sarcasmbote:latest .
   ```

3. Run the Docker container:
   ```bash
   docker run  --env-file=.env sarcasmbot:latest
   ```

4. Bot will connect to discord - start getting sarcastic
