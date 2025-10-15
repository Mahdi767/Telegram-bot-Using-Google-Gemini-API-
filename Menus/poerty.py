import requests
from telegram import Update,ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder,CommandHandler,MessageHandler,filters,ContextTypes,ChatMemberHandler
import os



def poetry_menu():
    return ReplyKeyboardMarkup(
        [
            ["📝 Generate Poem"],
            ["⬅️ Main Menu"]
        ],
        resize_keyboard=True
    )


