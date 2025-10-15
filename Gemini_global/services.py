import os
from dotenv import load_dotenv
import google.generativeai as genai
from google.api_core.exceptions import DeadlineExceeded, GoogleAPIError 
from google.generativeai.types import RequestOptions 

# env load
load_dotenv()


GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")



def gemini_reply(user_text, timeout_seconds=10): 
    try:
        gemini_api_key = os.getenv("GEMINI_API_KEY")

        if not gemini_api_key:
            return "Error: GEMINI_API_KEY not found in environment variables. Please check your .env file."

        genai.configure(api_key=gemini_api_key)

        model = genai.GenerativeModel('models/gemini-flash-latest')

       
        request_options = RequestOptions(timeout=timeout_seconds) #time out set


        response = model.generate_content(user_text, request_options=request_options)

        return response.text
    except DeadlineExceeded:
        return f"Sorry, the Gemini API took longer than {timeout_seconds} seconds to respond. Your message might be too long or detailed. Please try asking for a shorter response."
    except GoogleAPIError as e:
        return f"A Google API error occurred: {e}"
    except Exception as e:
        return f"An unexpected error occurred: {e}"



# Source code link:https://github.com/google-gemini/deprecated-generative-ai-python/blob/main/docs/api/google/generativeai.md


