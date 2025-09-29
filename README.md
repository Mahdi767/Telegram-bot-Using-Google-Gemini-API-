# Telegram Bot (Using Google Gemini API)

A Telegram bot that lets users chat with Google Gemini AI directly from Telegram.  
The bot can also respond to questions about its creator and handles slow or long messages gracefully.

---

## Features

- Chat with Gemini AI naturally.
- `/start`, `/help`, and `/stop` commands.
- Clears chat history when `/stop` is used.
- Handles slow responses with a timeout message.

---

## Commands

| Command | Description |
|---------|-------------|
| /start  | Start a new chat with Gemini AI. |
| /help   | Show available commands. |
| /stop   | End chat and delete chat history. |

---

## Installation
```bash
1. Clone the repo:

git clone https://github.com/yourusername/telegram-gemini-bot.git
cd telegram-gemini-bot

2. Create a virtual environment:

python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

3. Install dependencies:

pip install -r requirements.txt

4. Create a .env file in the project root:

TELEGRAM_TOKEN=your_telegram_bot_token
GEMINI_API_KEY=your_gemini_api_key




