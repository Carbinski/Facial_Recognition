import requests

def request_api() -> dict:
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "lat": 33.628,
        "lon": -117.927,
        "appid": "05a8b17327695560a4a1cd8fd0c11617",
        "units": "imperial", 
        "lang": "en"
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print("Error:", response.status_code, response.text)
        return {}

# Example usage
if __name__ == "__main__":
    results = request_api()