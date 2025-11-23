import csv
import os
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError
from telegram import ReplyKeyboardMarkup
from Gemini_global.services import gemini_reply

ROUTINE_FILE = Path(__file__).resolve().parents[1] / "Gemini_global" / "routine.csv"

def class_routine_menu():
    return ReplyKeyboardMarkup([["📅 Refresh Routine"],
                                 ["⬅️ Main Menu"]], resize_keyboard=True)
test_time_1 = datetime(2025, 11, 20, 11, 30) 
def get_class_routine_message():
    try:
        tz = ZoneInfo(os.getenv("ROUTINE_TIMEZONE", "Asia/Dhaka"))
    except ZoneInfoNotFoundError:
        tz = None
    # now = test_datetime if test_datetime else datetime.now(tz)
    now = datetime.now(tz)
    if not ROUTINE_FILE.exists():
        return "Routine file not found."

    with ROUTINE_FILE.open("r", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    today_rows = [r for r in rows if r.get("Day", "").lower() == now.strftime("%A").lower()]
    active, upcoming = None, None
    
    for row in today_rows:
        start = datetime.strptime(row["StartTime"].strip(), "%I:%M %p").time()
        end = datetime.strptime(row["EndTime"].strip(), "%I:%M %p").time()
        if start <= now.time() <= end:
            active = row
            break
        if start > now.time() and (not upcoming or start < datetime.strptime(upcoming["StartTime"].strip(), "%I:%M %p").time()):
            upcoming = row

    prompt = (
        f"Current time: {now.strftime('%A, %I:%M %p')}. "
        f"Active Class: {active if active else 'None'}. "
        f"Next Class: {upcoming if upcoming else 'None'}. "
        "If there is an active class, describe it briefly (Course, Room, Faculty). "
        "If no active class, say 'There is no class now' and mention the next class if any. "
        "Keep it concise."
    )
    
    return gemini_reply(prompt, timeout_seconds=10) or "Could not fetch routine info."