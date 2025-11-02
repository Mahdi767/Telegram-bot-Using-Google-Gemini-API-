import requests
from telegram import Update,ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder,CommandHandler,MessageHandler,filters,ContextTypes,ChatMemberHandler
import os
from Gemini_global.img_service import generate_image_from_prompt



def generate_img_menu():
    # This menu is shown when the user is in the image generation state.
    # The user will type a prompt, so we only need a back button.
    return ReplyKeyboardMarkup(
        [
            ["⬅️ Main Menu"]
        ],
        resize_keyboard=True
    )


def get_image_from_text(text: str, timeout_seconds: int = 8) -> str:

    response_text =generate_image_from_prompt(text, timeout_seconds=timeout_seconds)
    return response_text