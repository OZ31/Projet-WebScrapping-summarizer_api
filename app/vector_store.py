import faiss
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer

def build_faiss_index(articles):
    vectorizer = TfidfVectorizer()
    texts = [article['text'] for article in articles] 
    vectors = vectorizer.fit_transform(texts).toarray().astype('float32') 
    dimension = vectors.shape[1] 
    faiss_index = faiss.IndexFlatL2(dimension) 
    faiss_index.add(vectors) 
    return faiss_index, vectorizer

def search_similar_articles(query, faiss_index, vectorizer, articles, k=5): 
    query_vector = vectorizer.transform([query]).toarray().astype('float32')
    distances, indices = faiss_index.search(query_vector, k)
    similar_articles = [articles[i] for i in indices[0]]
    return similar_articles

def generate_vector(text):
    """
    Génère un vecteur TF-IDF pour un texte donné.
    """
    vectorizer = TfidfVectorizer()
    vector = vectorizer.fit_transform([text])
    return vector, vectorizer

def save_vector(vector, vectorizer, filename="vector_store.pkl"):
    """
    Sauvegarde le vecteur et le vectorizer dans un fichier.
    """
    with open(filename, "wb") as f:
        pickle.dump({"vector": vector, "vectorizer": vectorizer}, f)

def load_vector(filename="vector_store.pkl"):
    """
    Charge le vecteur et le vectorizer depuis un fichier.
    """
    with open(filename, "rb") as f:
        data = pickle.load(f)
    return data["vector"], data["vectorizer"]

print("L'indexation des vecteurs et la recherche d'articles similaires ont été implémentées avec succès!")
