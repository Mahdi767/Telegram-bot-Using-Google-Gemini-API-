import requests
from urllib.parse import quote
from io import BytesIO

def generate_image_from_prompt(prompt, timeout_seconds=60):
    encoded_prompt = quote(prompt)
    url = f"https://image.pollinations.ai/prompt/{encoded_prompt}"
    params = {"width": 1280, "height": 720, "model": "flux"}

    try:
        response = requests.get(url, params=params, timeout=timeout_seconds)
        response.raise_for_status()

        # Return image data in BytesIO (jate telegram img sent korte pare)
        image_data = BytesIO(response.content)
        return image_data, None

    except requests.exceptions.RequestException as e:
        print("Error generating image:", e)
        return None, str(e)


# https://github.com/pollinations/pollinations/tree/master source code