import requests
from dotenv import load_dotenv
import os

def request_api() -> dict:

    # get api key
    load_dotenv()
    api_key = os.getenv("WEATHER_API")

    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "lat": 33.628,
        "lon": -117.927,
        "appid": api_key,
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