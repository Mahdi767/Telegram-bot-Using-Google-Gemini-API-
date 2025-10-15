import requests
from telegram import Update,ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder,CommandHandler,MessageHandler,filters,ContextTypes,ChatMemberHandler
import os



def jokes_menu():
    return ReplyKeyboardMarkup(
        [
            ["🤣 Generate Joke"],
            ["⬅️ Main Menu"]
        ],
        resize_keyboard=True
    )