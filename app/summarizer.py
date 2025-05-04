import requests
import os
from dotenv import load_dotenv

# Charger les variables d'environnement
load_dotenv()

def summarize_text(text):
    """
    Génère un résumé pour un texte donné en utilisant l'API Gemini.
    """
    gemini_api_key = os.getenv("GEMINI_API_KEY")
    if not gemini_api_key:
        raise ValueError("Clé API Gemini manquante")

    gemini_url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={gemini_api_key}"
    payload = {
        "contents": [
            {
                "parts": [
                    {
                        "text": f"Résume cet article en quelques phrases :\n\n{text}"
                    }
                ]
            }
        ]
    }

    response = requests.post(
        gemini_url,
        headers={"Content-Type": "application/json"},
        json=payload
    )

    if response.status_code != 200:
        raise Exception(f"Erreur API Gemini : {response.text}")

    summary = response.json().get("contents", [{}])[0].get("parts", [{}])[0].get("text", "Résumé non disponible")
    return summary

