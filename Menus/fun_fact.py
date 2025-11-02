import requests
from telegram import Update,ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder,CommandHandler,MessageHandler,filters,ContextTypes,ChatMemberHandler
import os
from Gemini_global.services import gemini_reply

#  Fun Fact Menu
def fun_fact_menu():
    return ReplyKeyboardMarkup(
        [
            ["🤯 Generate Fun Fact"],
            ["⬅️ Main Menu"]
        ],
        resize_keyboard=True
    )



def generate_fact():
    prompt = ("Give me a fun, interesting, and surprising fact. "
          "Keep it concise (one or two sentences). "
          "Make sure it's something not widely known and suitable for a general audience.")
    response =  gemini_reply(prompt)
    if not response:
        return "Something went wrong!"

    return response.strip()