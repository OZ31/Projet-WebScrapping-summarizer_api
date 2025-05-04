import newspaper

def fetch_article(url):
    """
    Récupère les données d'un article à partir de son URL.
    """
    article = newspaper.Article(url=url, language='fr')
    article.download()
    article.parse()
    article_data = {
        "title": article.title,
        "text": article.text,
        "authors": article.authors,
        "published_date": article.publish_date,
        "top_image": article.top_image,
        "videos": article.movies,
    }
    return article_data

print("Le scraper a été implémenté avec succès!")
