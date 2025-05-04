from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn
from newspaper import Article
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Charger les variables d'environnement
load_dotenv()

# Configuration de l'API Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel('models/gemini-1.5-flash-001')

app = FastAPI(title="Article Summarizer API")

class URLRequest(BaseModel):
    url: str

@app.get("/")
async def root():
    return {"message": "Bienvenue sur l'API de résumé d'articles"}

@app.post("/summarize")
async def summarize_article(request: URLRequest):
    try:
        # Récupération de l'article
        article = Article(request.url)
        article.download()
        article.parse()
        
        # Vérification que l'article a bien été récupéré
        if not article.text:
            raise HTTPException(status_code=400, detail="Impossible de récupérer le contenu de l'article")
        
        # Génération du résumé avec Gemini
        prompt = f"""Résume cet article de presse en quelques phrases claires et concises :
        
        {article.text}
        """
        
        response = model.generate_content(prompt)
        summary = response.text
        
        return {
            "title": article.title,
            "summary": summary,
            "url": request.url
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
