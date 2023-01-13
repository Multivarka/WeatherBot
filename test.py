import requests
#api.openweathermap.org/data/2.5/forecast/daily?lat={lat}&lon={lon}&cnt=4&appid=bb1b18ffa613f7f90eb41448dfa20793
def get_weather(lat, lon):
    r = requests.get(
        f"https://pro.openweathermap.org/data/2.5/forecast/hourly?lat=44.34&lon=10.99&appid=bb1b18ffa613f7f90eb41448dfa20793")
    data = r.json()
    print(data)


get_weather(55.12, 37.91)