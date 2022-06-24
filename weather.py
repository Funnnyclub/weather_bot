import datetime

import requests
from pprint import pprint
from config import token_weather

def get_weather(city, token_weather):

    code_to_smile = {
        "Clear": "Ясно \U00002600",
        "Clouds": "Облачно \U00002601",
        "Rain": "Дождь \U00002614",
        "Drizzle": "Дождь \U00002614",
        "Thunderstorm": "Гроза \U000026A1",
        "Mist": "Туман \U0001f32b",
        "Snow": "Снег \U0001f328",

    }

    try:
        r = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={token_weather}&units=metric")
        data =r.json()
        #pprint(data)
        city = data["name"]
        weather_description = data["weather"][0]["main"]
        if weather_description in code_to_smile:
            wd =code_to_smile[weather_description]
        else:
            wd =" Look at the window"
        cur_weather = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        wind = data ["wind"]["speed"]
        sunrise_time = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
        sunset_time = datetime.datetime.fromtimestamp(data["sys"]["sunset"])
        lenght_of_the_day = sunset_time - sunrise_time
        print(f"***{datetime.datetime.now().strftime('%Y-%m-$d %H:%M')}***"
            f"Погода в городе: {city}\nТемпература: {cur_weather}\nОщущается как: {feels_like}C  {wd}\nСкорость ветра: {wind}\nВремя рассвета: {sunrise_time}\nВремя заката: {sunset_time}\nДлительность дня: {lenght_of_the_day}")
    except Exception as ex:
        print(ex)
        print("Проверьте название города")
def main():
    city = input("Введите Город: ")
    get_weather(city,token_weather)
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()