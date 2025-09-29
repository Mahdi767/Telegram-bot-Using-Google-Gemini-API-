import requests
from telegram import Update,ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder,CommandHandler,MessageHandler,filters,ContextTypes,ChatMemberHandler
import os
from dotenv import load_dotenv
load_dotenv()


# user name : @AI_testGeminibot
#The token of telegram
TELEGRAM_TOKEN = TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")

#Gemini API
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_API_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent"

# user storage
user_sessions ={}


# gemini fn
def gemini_reply(user_text):
    # instruction_text = "From now on, if anyone asks 'Who created you?' or 'Who made you?' or similar questions in any language, your answer is 'I was created by Mahdi.' If they ask in a different language, try to translate this answer appropriately. For example, if asked in Arabic 'من أنشأك؟', you should reply 'لقد صنعت بواسطة مهدي.' Now, proceed with the user's request: "
    # full_prompt_with_instruction = instruction_text + user_text

    payload = {
        "contents": [{"parts": [{"text": user_text}]}]
    }
    headers = {
        "Content-Type": "application/json",
        "X-goog-api-key": GEMINI_API_KEY  
    }

    try:
        response = requests.post(GEMINI_API_URL, json=payload, headers=headers,timeout=5)
        if response.status_code == 200:
            data = response.json()
            candidates = data.get("candidates")
            if candidates and len(candidates) > 0:
                parts = candidates[0].get("content", {}).get("parts")
                if parts and len(parts) > 0:
                    return parts[0].get("text", "No text found.")
            return "Error: Gemini returned empty response."
        return f"Error: Status code {response.status_code}"
    except requests.exceptions.Timeout:
        return "Sorry, Gemini is taking too long to respond. Your message might be too long or detailed. Please try asking for a shorter response, as the API has limits"
    except Exception as e:
        return f"Error: {e}"


# command handler
async def start(update:Update,context:ContextTypes.DEFAULT_TYPE):
    # target --> /start command
    # clear previous chat history
    # y/n option for user

    user_id = update.message.from_user.id
    user_sessions[user_id] = []

    keyboard =  [["Yes, Chat with Gemini"], ["No, Thanks"]]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

    await update.message.reply_text(
        "Hi! would you like to chat with gemini?",
        reply_markup= reply_markup
    )


async def help_command(update:Update, context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Commands:\n"
        "/start - Start chatting with Gemini\n"
        "/help - Show this message\n"
        "/stop - Stop chat and delete history\n\n"
        "You can also type messages directly to chat with Gemini."
    )


async def stop_chat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Stops the chat and clears user history."""
    user_id = update.message.from_user.id
    if user_id in user_sessions:
        user_sessions.pop(user_id, None)
        await update.message.reply_text("Chat stopped. All history deleted.")
    else:
        await update.message.reply_text("You don't have an active chat to stop.")


async def chat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id
    text = update.message.text.strip()

    #  user has not started chat
    if user_id not in user_sessions:
        await update.message.reply_text("Please start a new chat using /start")
        return

    # if no thanks then del everything
    if text.lower() == "no, thanks":
        user_sessions.pop(user_id, None)
        await update.message.reply_text("Okay! You can start anytime with /start")
        return

    # if yes then this
    if text.lower() == "yes, chat with gemini":
        await update.message.reply_text("Great! You can start typing your messages. Type /stop to end chat.")
        return

    # save user msg
    user_sessions[user_id].append(text)

  

    # gemini rply
    reply = gemini_reply(text)
    user_sessions[user_id].append(reply)
    await update.message.reply_text(reply)


# if user left the chat
async def handle_leave(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.chat_member.from_user.id
    if user_id in user_sessions:
        user_sessions.pop(user_id, None)
        print(f"Deleted history for user {user_id} (left chat).")


#  commands 
def main():
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("stop", stop_chat))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, chat))
    app.add_handler(ChatMemberHandler(handle_leave, chat_member_types=["left"]))
    print(" Gemini is running...")
    app.run_polling()


if __name__ == "__main__":
    main()
