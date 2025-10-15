import requests
from telegram import Update,ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder,CommandHandler,MessageHandler,filters,ContextTypes,ChatMemberHandler
import os



def motivation_menu():
    return ReplyKeyboardMarkup(
        [
            ["🌅 Get Daily Motivation"],
            ["⬅️ Main Menu"]
        ],
        resize_keyboard=True
    )