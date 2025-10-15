from email import message
import requests
from telegram import Update,ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder,CommandHandler,MessageHandler,filters,ContextTypes,ChatMemberHandler
import os
from Gemini_global.services import gemini_reply
from Menus.fun_fact import fun_fact_menu
from Menus.islamic_menu import islamic_menu,get_random_quran_verse,get_random_hadith
from Menus.jokes import jokes_menu
from Menus.Life_tips import life_tips_menu
from Menus.quiz import quiz_menu
from Menus.motivation import motivation_menu
from Menus.poerty import poetry_menu
from Menus.quotes import quotes_menu, generate_quote
from Menus.direct_chat import direct_chat_menu,direct_chat
from Database.database import init_db,save_user_to_db

from dotenv import load_dotenv
load_dotenv()

# Kill python --> taskkill /F /IM python.exe
# user name : @AI_testGeminibot
#The token of telegram
TELEGRAM_TOKEN = TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")

#Gemini API
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_API_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent"

# user storage
user_sessions ={}

# ei option gula main e thakbe
def main_menu_key():
    return ReplyKeyboardMarkup(
        [
            ["💬 Direct Chat", "💡 Quotes"],
            ["😂 Jokes", "🤯 Fun Fact"],
            ["🧘 Life Tips", "🎮 Quiz"],
            ["☪️ Islamic Reminder", "📅 Daily Motivation"]
        ],
        resize_keyboard=True
    )

# gemini fn

init_db()
# command handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    save_user_to_db(user.id, user.first_name, user.username)

    user_sessions[user.id] = {"state": "main_menu"}

    await update.message.reply_text(
        f"Welcome {user.first_name}! 🎉 Choose an option:",
        reply_markup=main_menu_key()
    )

async def help_command(update:Update, context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Commands:\n"
        "/start - Show main menu\n"
        "/help - Show help\n"
        "/stop - Stop chat and delete history\n\n"
        "Use the buttons to navigate menus."
    )


async def stop_chat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Stops the chat and clears user history."""
    user_id = update.message.from_user.id
    if user_id in user_sessions:
        user_sessions.pop(user_id, None)
        await update.message.reply_text("Chat stopped. All history deleted.")
    else:
        await update.message.reply_text("You don't have an active chat to stop.")

# The main logic
async def chat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id
    text = update.message.text.strip()

    if user_id not in user_sessions:
        await update.message.reply_text("Please start a new chat using /start")
        return

    state = user_sessions[user_id]["state"]

    # Always allow going back to main menu
    if text == "⬅️ Main Menu" or text.lower() == "/back":
        user_sessions[user_id]["state"] = "main_menu"
        await update.message.reply_text("Back to Main Menu:", reply_markup=main_menu_key())
        return



# inside chat()
    if state == "main_menu":
        menus = {
            "💬 Direct Chat": {"state": "direct_chat", "msg": "You are now in Direct Chat mode.", "keyboard":  direct_chat_menu()},
            "😂 Jokes": {"state": "jokes_menu", "msg": "Jokes Menu", "keyboard": jokes_menu()},
            "💡 Quotes": {"state": "quotes_menu", "msg": "Quotes Menu", "keyboard": quotes_menu()},
            "🤯 Fun Fact": {"state": "fun_fact_menu", "msg": "Fun Fact Menu", "keyboard": fun_fact_menu()},
            "🎮 Quiz": {"state": "quiz_menu", "msg": "Quiz Menu", "keyboard": quiz_menu()},
            "📅 Daily Motivation": {"state": "motivation_menu", "msg": "Motivation Menu", "keyboard": motivation_menu()},
            "☪️ Islamic Reminder": {"state": "islamic_menu", "msg": "Islamic Menu", "keyboard": islamic_menu()},
            "🧘 Life Tips": {"state": "life_tips_menu", "msg": "Life Tips Menu", "keyboard": life_tips_menu()}
        }

        # safely get menu, returns None if text not in dict
        menu = menus.get(text)

        if menu is not None:
            user_sessions[user_id]["state"] = menu["state"]
            await update.message.reply_text(menu["msg"], reply_markup=menu["keyboard"])
        else:
            await update.message.reply_text("Please use the menu buttons.", reply_markup=main_menu_key())

    elif state == "quotes_menu":
        if text == "✨ Generate Quote":
            quote = generate_quote()
            await update.message.reply_text(quote, reply_markup=quotes_menu())
        else:
            await update.message.reply_text("Please use the menu buttons.", reply_markup=quotes_menu())
        return
    elif state == "islamic_menu":
        if text == "📖 Quran Verse":
            random_verse = get_random_quran_verse()
            await update.message.reply_text(random_verse,reply_markup=islamic_menu())
        elif text == "📜 Hadith Verse":
            random_hadith = get_random_hadith()
            await update.message.reply_text(random_hadith,reply_markup=islamic_menu())
        else:
            await update.message.reply_text("Please use the menu buttons.", reply_markup=islamic_menu())

    elif state == "direct_chat":

        await update.message.reply_text("Thinking...", reply_markup=direct_chat_menu()) # Give immediate feedback

        gemini_answer = direct_chat(text,timeout_seconds=8)

        await update.message.reply_text(gemini_answer, reply_markup=direct_chat_menu())
  





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
