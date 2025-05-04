#### API de Résumé d'Articles

Cette application permet de récupérer et de résumer des articles web en utilisant une API
- 'main.py' : Point d'entrée de l'API FastAPI.
- 'app/scraper.py' : Contient la logique pour extraire les articles.
- 'app/summarizer.py' : Implémente le résumé des articles avec l'API Gemini.
- 'app/vector_store.py' : Gère l'indexation et la recherche d'articles similaires.

# Installation

1. Clonez ce dépôt
2. Installez les dépendances :

pip install -r requirements.txt

3. Créez un fichier '.env' à la racine du projet et ajoutez votre clé API OpenAI :

GEMINI_API_KEY=""


# Lancement de l'api :
python main.py

- L'API est disponible à l'adresse : `http://localhost:8000`

# Test :

curl -X POST "http://localhost:8000/summarize" \
     -H "Content-Type: application/json" \
     -d '{"url": "https://exemple.com/article"}'


Si tout fonctionne bien, l'api enverra une réponse de ce type :

    - titre de l'article.
    - résumé généré par l'IA.
    - Url de l'article.

# Pour le déploiement sur docker
docker build -t article-summarizer .
docker run -d -p 8000:8000 --name article-summarizer-container article-summarizer
