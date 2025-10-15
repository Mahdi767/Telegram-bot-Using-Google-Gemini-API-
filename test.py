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
