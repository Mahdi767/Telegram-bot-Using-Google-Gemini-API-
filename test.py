# def gemini_reply(user_text):

    # payload = {
    #     "contents": [{"parts": [{"text": user_text}]}]
    # }
    # headers = {
    #     "Content-Type": "application/json",
    #     "X-goog-api-key": GEMINI_API_KEY  
    # }

    # try:
    #     response = requests.post(GEMINI_API_URL, json=payload, headers=headers,timeout=5)
    #     if response.status_code == 200:
    #         data = response.json()
    #         candidates = data.get("candidates")
    #         if candidates and len(candidates) > 0:
    #             parts = candidates[0].get("content", {}).get("parts")
    #             if parts and len(parts) > 0:
    #                 return parts[0].get("text", "No text found.")
    #         return "Error: Gemini returned empty response."
    #     return f"Error: Status code {response.status_code}"
    # except requests.exceptions.Timeout:
    #     return "Sorry, Gemini is taking too long to respond. Your message might be too long or detailed. Please try asking for a shorter response, as the API has limits"
    # except Exception as e:
    #     return f"Error: {e}"

import google.generativeai as genai
import os
from dotenv import load_dotenv
load_dotenv()
# IMPORTANT: Replace "YOUR_API_KEY" with your actual Gemini API key,
# or ensure it's set as an environment variable named GEMINI_API_KEY.
# For example:
# os.environ["GEMINI_API_KEY"] = "YOUR_ACTUAL_API_KEY_HERE"

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("Error: GEMINI_API_KEY environment variable not set.")
    print("Please set it or replace os.environ.get('GEMINI_API_KEY') with your key.")
else:
    genai.configure(api_key=api_key)
    
    print("Models supporting 'generateContent':")
    try:
        for m in genai.list_models():
            if 'generateContent' in m.supported_generation_methods:
                print(f"- {m.name}")
    except Exception as e:
        print(f"An error occurred while listing models: {e}")

