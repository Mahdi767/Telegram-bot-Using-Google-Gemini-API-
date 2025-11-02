
import requests
from telegram import Update,ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder,CommandHandler,MessageHandler,filters,ContextTypes,ChatMemberHandler
import os

from Gemini_global.services import gemini_reply



def mythvsfact_menu():
    return ReplyKeyboardMarkup(
        [
            ["🧐 Generate Myth vs. Fact"],
            ["⬅️ Main Menu"]
        ],
        resize_keyboard=True
    )

def myth_vs_fact():
    prompt = ("Tell me a common myth and the true fact that debunks it. "
          "Present the answer in a 'Myth: ... Fact: ...' format. "
          "Keep the entire response concise (two to three sentences total). "
          "Make sure the topic is suitable for a general audience.")
    response = gemini_reply(prompt)
    if not response:
        return "Something Went Wrong!"
    return response.strip()

