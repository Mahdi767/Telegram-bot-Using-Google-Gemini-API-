# Lumora AI — Telegram Bot powered by Google Gemini

Lumora AI is a Python Telegram bot that connects your chat to Google’s Gemini models for smart conversations, creative generation, and utility features — all from Telegram.

- Language: Python
- Platform: Telegram Bot API
- Model: Google Gemini (configurable)
- Modes: Reply Keyboard buttons and text commands

> Tip: Use `/start` to see Lumora AI’s menu inside Telegram.

---

## Features

Current keyboard (as shown in the screenshot) includes:

- 💬 Direct Chat — Converse with Gemini about anything.
- 💡 Quotes — Get inspirational or themed quotes.
- 🧾 Story — Generate short stories from prompts or themes.
- 🤯 Fun Fact — Share surprising facts.
- 🖼️ Generate Image — Create images from prompts (if image generation is enabled in code/config).
- 🎮 Quiz — Quick Q&A; can be general knowledge or themed.
- ☪️ Islamic Reminder — Send helpful reminders (e.g., daily ayah/hadith, duas) if configured.
- 🤓 Myth vs. Fact — Present a statement and clarify whether it’s myth or fact.

Notes:
- Buttons trigger their respective handlers in the bot’s code.
- Most features also work with commands (see Commands section) if implemented in your code.

---

## Prerequisites

- Python 3.9+
- A Telegram Bot Token from [@BotFather](https://t.me/BotFather)
- A Google Gemini API key from [Google AI Studio](https://aistudio.google.com/app/apikey)
- Git and pip

---

## Quick Start

1) Clone the repository
```bash
git clone https://github.com/Mahdi767/Telegram-bot-Using-Google-Gemini-API-.git
cd Telegram-bot-Using-Google-Gemini-API-
```

2) Create a virtual environment and install dependencies
```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

pip install -r requirements.txt
```

3) Configure environment variables

Create a file named `.env` in the project root (or set these in your environment):

```bash
# Required
TELEGRAM_BOT_TOKEN=YOUR_TELEGRAM_BOT_TOKEN
GEMINI_API_KEY=YOUR_GOOGLE_GEMINI_API_KEY

# Common settings
GEMINI_MODEL=gemini-1.5-flash
SYSTEM_PROMPT=You are Lumora AI, a helpful and kind assistant in a Telegram chat.
TEMPERATURE=0.7
MAX_TOKENS=2048

# Optional feature toggles (use 1/0 as needed, only if your code reads them)
ENABLE_IMAGE=1
ENABLE_QUIZ=1
ENABLE_ISLAMIC_REMINDER=1
ENABLE_MYTH_VS_FACT=1

# Optional runtime settings
TIMEZONE=UTC
ADMIN_USER_IDS= # e.g., 123456789,987654321
ALLOWED_CHAT_IDS= # comma-separated list if you want to restrict usage
```

4) Run the bot
```bash
python bot.py
```

---

## Commands and Usage

- `/start` — Show the Lumora AI keyboard.
- `/help` — Display usage tips.
- `/reset` — Reset conversation context (if your code supports it).

Mapped to keyboard features (typical examples; adjust to your handlers):

- Direct Chat:
  - Send any message, or use `/chat Your question here`
- Quotes:
  - Press “Quotes” or `/quote [topic]`
- Story:
  - Press “Story” or `/story Write a short sci‑fi story about a friendly robot`
- Fun Fact:
  - Press “Fun Fact” or `/funfact [topic]`
- Generate Image:
  - Press “Generate Image” or `/image A serene lake at sunrise in watercolor style`
  - Requires image generation to be enabled and supported in code.
- Quiz:
  - Press “Quiz” or `/quiz [category]` then follow the prompts
- Islamic Reminder:
  - Press “Islamic Reminder” or `/reminder [daily|ayah|hadith|dua]`
- Myth vs. Fact:
  - Press “Myth vs. Fact” or `/mythvsfact Coffee stunts your growth`

If any command isn’t wired in your code, use the button instead or update handlers to match these names.

---

## Image Generation

If your repository enables image generation through Google’s Generative AI (e.g., Gemini image generation/Image API), ensure:
- The correct SDK is installed and imported.
- The model name and endpoint are set (e.g., `imagen-3` or the currently available image-capable model).
- `ENABLE_IMAGE=1` is set if your code checks this flag.

If image generation isn’t set up in the code yet, you can:
- Hide the “Generate Image” button, or
- Implement the handler to call the image generation API, save the image, and send it as a Telegram photo.

---

## Deployment

### Long polling (simple)
- Just run `python bot.py` on a VM/VPS or PaaS service (Railway/Render/Fly.io).
- Use a process manager like `pm2`, `supervisord`, or `systemd` to keep it running.

### Webhook (production)
- Host a public HTTPS endpoint (Cloud Run, Render, Railway, etc.).
- Set the Telegram webhook to your URL:
  ```bash
  curl "https://api.telegram.org/bot$TELEGRAM_BOT_TOKEN/setWebhook?url=YOUR_HTTPS_URL"
  ```
- Ensure your app listens for Telegram updates at the configured route.

Docker (optional; only if a Dockerfile is present):
```bash
docker build -t lumora-ai-bot .
docker run --rm -e TELEGRAM_BOT_TOKEN=YOUR_TOKEN \
               -e GEMINI_API_KEY=YOUR_KEY \
               -e GEMINI_MODEL=gemini-1.5-flash \
               lumora-ai-bot
```

---

## Configuration Notes

- Models:
  - `gemini-1.5-flash` — fast and cost‑effective
  - `gemini-1.5-pro` — more capable, higher cost
- Safety and rate limits:
  - Configure safety/filters per your code
  - Respect API quotas to avoid throttling
- Persistence:
  - If you store conversation context, ensure you handle privacy and data retention responsibly.

---

## Project Structure (example)

```
.
├── bot.py
├── handlers/               # feature handlers (if you split modules)
├── utils/                  # helpers (logging, prompts, etc.)
├── requirements.txt
├── README.md
└── .env                    # not committed
```

Your actual structure may differ; see the code for exact entry points and handlers.

---

## Contributing

- Pull requests are welcome
- For significant changes, open an issue to discuss the proposal first
- Please follow conventional commit messages if possible


---

## Acknowledgements

- Google Gemini API (Google AI Studio)
- Telegram Bot Platform
