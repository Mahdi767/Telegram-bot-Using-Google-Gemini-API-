import requests
from telegram import Update,ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder,CommandHandler,MessageHandler,filters,ContextTypes,ChatMemberHandler
import os


#  Fun Fact Menu
def fun_fact_menu():
    return ReplyKeyboardMarkup(
        [
            ["🤯 Generate Fun Fact"],
            ["⬅️ Main Menu"]
        ],
        resize_keyboard=True
    )