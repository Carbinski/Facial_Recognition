from APIs import Spaceflight, Currents, Weather
from tts import run_tts

def get_news(type: str, amount: int) -> list:
    if type == "space":
        return Spaceflight.request_api(amount)
    elif type == "top":
        return Currents.request_api(amount)

def report_news(type: str, amount: int):
    news = get_news(type, amount)
    run_tts(f"Today's {type} Headlines!")
    for article in news:
        run_tts(article['title'])
        run_tts(article['summary'])

def report_weather():
    weather = Weather.request_api()
    try:
        run_tts(f"Right now its {weather["main"]["temp"]} degrees. It feels like {weather["main"]["feels_like"]} and is {weather["weather"][0]["main"]} outside. The humidity is {weather["main"]["humidity"]} and the wind speed is {weather["wind"]["speed"]}")
    except KeyError:
        run_tts("We're unable to access the weather rightn now")

if __name__ == "__main__":
    # news = get_news("space", 3)
    # report_news("space", news)

    report_weather()