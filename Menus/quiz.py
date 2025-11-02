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

def quiz_difficulity():
    return ReplyKeyboardMarkup(
        [
       ["🟢 Easy", "🟠 Medium", "🔴 Hard"],
            ["⬅️ Main Menu"],
        ],
        resize_keyboard=True

    )


def quiz_category_menu():
    return ReplyKeyboardMarkup(
        [
            ["🧠 General Knowledge","💻 Technology"],
            ["🔬 Science", "📜 History"],
            ["⚽ Sports", "🗺️ Geography"],
            ["⬅️ Back to Difficulty", "⬅️ Main Menu"]
        ],
        resize_keyboard=True
    )