
import requests
from telegram import Update,ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder,CommandHandler,MessageHandler,filters,ContextTypes,ChatMemberHandler
import os
from Gemini_global.services import gemini_reply



#  Quotes Menu
def quotes_menu():
    return ReplyKeyboardMarkup(
        [
            ["✨ Generate Quote"],
            ["⬅️ Main Menu"]
        ],
        resize_keyboard=True
    )


def generate_quote():
    prompt =  ("Give a short inspirational quote (one or two sentences). "
        "Keep it original and uplifting. "
        "Also provide a short author name at the end, like '- Author Name'.")
    response =  gemini_reply(prompt)
    if not response:
        return "Something went wrong!"

    return response.strip()

