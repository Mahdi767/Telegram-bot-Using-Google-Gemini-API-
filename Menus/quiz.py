import requests
from telegram import Update,ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder,CommandHandler,MessageHandler,filters,ContextTypes,ChatMemberHandler
import os



def quiz_menu():
    return ReplyKeyboardMarkup(
        [
            ["❓ Start Quiz"],
            ["⬅️ Main Menu"]
        ],
        resize_keyboard=True
    )