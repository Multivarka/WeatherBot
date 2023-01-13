import requests
import config
import datetime

class Weather:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon

    def get_weather(self):
        r = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?"
            f"lat={self.lat}&lon={self.lon}&appid={config.weather_api}&units=metric")
        data = r.json()
        city = data["name"]
        weather = [data["main"]["temp"], data["main"]["humidity"], data["main"]["pressure"]]
        sunrise = [datetime.datetime.fromtimestamp(data['sys']['sunrise']),
                   datetime.datetime.fromtimestamp(data['sys']['sunset'])]
        s = f"Погода в {city}\n" \
            f"Температура: {weather[0]}°C\n" \
            f"Влажность: {weather[1]}%\n" \
            f"Давление: {weather[2]} мм р.с.\n" \
            f"Восход в {sunrise[0].hour}:{sunrise[0].minute}, Закат в {sunrise[1].hour}:{sunrise[1].minute}"
        return s



def get_weather(lat, lon, token):
    try:
        r = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={token}&units=metric")
        data = r.json()
        city = data["name"]
        weather = [data["main"]["temp"], data["main"]["humidity"], data["main"]["pressure"]]
        sunrise = [datetime.datetime.fromtimestamp(data['sys']['sunrise']),
                   datetime.datetime.fromtimestamp(data['sys']['sunset'])]
        s = f"Погода в {city}\n" \
            f"Температура: {weather[0]}°C\n" \
            f"Влажность: {weather[1]}%\n" \
            f"Давление: {weather[2]} мм р.с.\n" \
            f"Восход в {sunrise[0].hour}:{sunrise[0].minute}, Закат в {sunrise[1].hour}:{sunrise[1].minute}"
        print(s)
    except Exception as ex:
        print(ex)


def main():
    get_weather(55.90, 37.58, config.weather_api)


if __name__ == "__main__":
    main()
