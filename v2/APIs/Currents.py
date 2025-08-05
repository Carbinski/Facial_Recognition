import requests

def request_api(amount: int) -> list:
    url = "https://api.currentsapi.services/v1/latest-news"
    headers = {
        "Authorization": "V0_7jJ_l3XAOI5PcEuw5cZ2b45o352bWv5GSPvRzl2O33tpH"
    }
    params = {
        "language": "en"
    }

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        articles = []
        i = 0
        for article in data["news"]:
            if i == amount:
                break
            
            formatted_article = {
                "title": article["title"],
                "summary": article["description"],  # ✅ renamed key
                "url": article["url"],
                "published": article["published"],
                "author": article.get("author"),
                "image": article.get("image"),
                "category": article.get("category", []),
                "language": article.get("language")
            }
            articles.append(formatted_article)

            i += 1
        return articles
    else:
        print("Error:", response.status_code, response.text)
        return []

# Example usage
if __name__ == "__main__":
    results = request_api(3)
    for article in results:
        print(article)