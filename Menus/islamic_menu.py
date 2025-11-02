

import requests
from telegram import Update,ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder,CommandHandler,MessageHandler,filters,ContextTypes,ChatMemberHandler
import os
import random





def islamic_menu():
    return ReplyKeyboardMarkup(
        [
            ["📖 Quran Verse", "📜 Hadith Verse"],
            ["⬅️ Main Menu"]
        ],
        resize_keyboard=True
    )




def get_random_quran_verse():
    verse_no = random.randint(1,6236)
    url = f"https://api.alquran.cloud/v1/ayah/{verse_no}/bn.bengali"
    try:
        res = requests.get(url,timeout=5)
        if res.status_code == 200:
           data = res.json()['data']
           text = data['text']
           surah = data['surah']['englishName']
           num = data['numberInSurah']

           return f"{text}\n-- Surah {surah},Verse {num}"
    except:
       return "Something went Wrong!"

# if __name__ == "__main__":
#  print(get_random_quran_verse())






def get_random_hadith():
    url = "https://cdn.jsdelivr.net/gh/fawazahmed0/hadith-api@1/editions/eng-nawawi.json"
    
    
    try:
        res = requests.get(url,timeout=5)
        if res.status_code == 200:
           data = res.json()
           collection_name = data.get('metadata', {}).get('name', 'Unknown Collection')
           hadiths = data.get('hadiths',[])
           if not hadiths:
               return "No hadith found"
           hadith = random.choice(hadiths)
           text = hadith.get('text','')
           num = hadith.get('hadithnumber','')

           return f"{text} \n {collection_name} - {num}"
    except Exception as e:
        return f"Something went wrong!{e}"
    
   

           
         

     


if __name__ == "__main__":
    print(get_random_hadith())
