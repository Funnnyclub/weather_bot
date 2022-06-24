import requests
import datetime
from config import tg_tolen, token_weather
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

bot = Bot(token = tg_tolen)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await  message.reply("Привет! Напиши название города и получи прогноз погоды!")

@dp.message_handler ()
async def get_weather (message: types.Message):
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
        r = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={token_weather}&units=metric")
        data = r.json()
        city = data["name"]
        weather_description = data["weather"][0]["main"]
        if weather_description in code_to_smile:
            wd = code_to_smile[weather_description]
        else:
            wd = " Look at the window"
        cur_weather = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        wind = data["wind"]["speed"]
        sunrise_time = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
        sunset_time = datetime.datetime.fromtimestamp(data["sys"]["sunset"])
        lenght_of_the_day = sunset_time - sunrise_time
        await message.reply(f"***{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}***"
              f"\nПогода в городе: {city}\nТемпература: {cur_weather}\nОщущается как: {feels_like}C  {wd}\nСкорость ветра: {wind}\nВремя рассвета: {sunrise_time}\nВремя заката: {sunset_time}\nДлительность дня: {lenght_of_the_day}\nХорошего вам дня!")
    except:
       await message.reply("Проверьте название города")

if __name__ == '__main__':
    executor.start_polling(dp)