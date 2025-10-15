
import requests
from telegram import Update,ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder,CommandHandler,MessageHandler,filters,ContextTypes,ChatMemberHandler
import os
from Gemini_global.services import gemini_reply
from google.generativeai.types import RequestOptions 
from google.api_core.exceptions import DeadlineExceeded



#  Quotes Menu
def direct_chat_menu():
    return ReplyKeyboardMarkup(
        [
            ["⬅️ Main Menu"]
        ],
        resize_keyboard=True
    )

def direct_chat(text: str, timeout_seconds: int = 8) -> str:
    """
    Processes a direct chat message by sending it to the Gemini API.
    This function acts as an intermediary, calling gemini_reply and returning its result.

    Args:
        text (str): The user's message to send to Gemini.
        timeout_seconds (int): The timeout for the Gemini API call in seconds.

    Returns:
        str: The response from Gemini, or an error message if an issue occurred (e.g., timeout).
    """
    # gemini_reply already handles the RequestOptions internally based on timeout_seconds
    # It will return the generated text or an error string (including timeout messages).
    response_text = gemini_reply(text, timeout_seconds=timeout_seconds)
    return response_text


    #         gemini_response_text = gemini_reply(text) # Pass the user's actual text

        # await update.message.reply_text(gemini_response_text, reply_markup=direct_chat_menu())