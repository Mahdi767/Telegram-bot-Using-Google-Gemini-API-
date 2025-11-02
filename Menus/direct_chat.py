
import requests
from telegram import Update,ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder,CommandHandler,MessageHandler,filters,ContextTypes,ChatMemberHandler
import os
from Gemini_global.services import gemini_reply
from google.generativeai.types import RequestOptions 
from google.api_core.exceptions import DeadlineExceeded



#  Quotes Menu
def direct_chat_menu():
    return ReplyKeyboardMarkup(
        [
            ["⬅️ Main Menu"]
        ],
        resize_keyboard=True
    )

def direct_chat(user_text: str, timeout_seconds: int = 20) -> str:

    response_text = gemini_reply(user_text, timeout_seconds=timeout_seconds)
    return response_text

        