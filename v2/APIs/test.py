import requests

def get_weather():
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "lat": 33.628,
        "lon": -117.927,
        "appid": "05a8b17327695560a4a1cd8fd0c11617",
        "units": "imperial",  # 'metric' for Celsius, 'imperial' for Fahrenheit
        "lang": "en"
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        weather = {
            "location": data.get("name"),
            "description": data["weather"][0]["description"],
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "wind_speed": data["wind"]["speed"]
        }
        print(weather)
        return weather
    else:
        print("❌ Error:", response.status_code, response.text)
        return None

# Example usage
if __name__ == "__main__":
    get_weather()