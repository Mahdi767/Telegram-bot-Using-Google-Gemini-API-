import requests
from telegram import Update,ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder,CommandHandler,MessageHandler,filters,ContextTypes,ChatMemberHandler
import os
from Gemini_global.services import gemini_reply


def story_menu():
    return ReplyKeyboardMarkup(
        [
            ["📜 Generate Story"],
            ["⬅️ Main Menu"]
        ],
        resize_keyboard=True
    )



def generate_story():
    prompt = ("Write a short original story in 3-5 sentences. "
          "Make it interesting and creative. "
          "Keep it suitable for all audiences.")


    response =  gemini_reply(prompt)
    if not response:
        return "Something went wrong!"

    return response.strip()
