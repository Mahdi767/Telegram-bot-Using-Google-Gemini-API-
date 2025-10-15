import requests
from telegram import Update,ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder,CommandHandler,MessageHandler,filters,ContextTypes,ChatMemberHandler
import os



def life_tips_menu():
    return ReplyKeyboardMarkup(
        [
            ["💡 Generate Life Tip"],
            ["⬅️ Main Menu"]
        ],
        resize_keyboard=True
    )