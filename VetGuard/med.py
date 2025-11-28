import os
import requests
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found!")

GEMINI_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent"

def get_medicine_suggestion(disease_name: str, animal: str) -> str:
    prompt = f"""
You are a veterinary assistant.

Provide the following for the disease: {disease_name}, in the animal: {animal}:

- If the disease is 'Healthy' or 'Normal Skin', return general well-being care only.
- Otherwise, suggest common veterinary medicines + treatment advice.
"""

    payload = {
        "contents": [{"parts": [{"text": prompt}]}]
    }

    response = requests.post(
        GEMINI_URL + f"?key={api_key}",
        json=payload
    )

    if response.status_code != 200:
        return f"Error: {response.text}"

    return response.json()["candidates"][0]["content"]["parts"][0]["text"]
