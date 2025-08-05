import requests

def request_api(amount: int) -> list:
    url = "https://api.spaceflightnewsapi.net/v4/articles/"
    params = {
        "ordering": "-published_at",
        "limit": amount
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        articles = response.json()["results"]
        return articles

    else:
        print("Failed to fetch news:", response.status_code)
        return []
    

if __name__ == "__main__":
    request_api(2)