import telebot
import config
from weather import Weather
from keyboards import ask_geo, ask_weather

bot = telebot.TeleBot(config.telegram_api)
weather = None


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.from_user.id, "Привет, для начала отправь мне свое местоположение", reply_markup=ask_geo())

#Получение локации
@bot.message_handler(content_types=['location'])
def location(message):
    global weather
    if message.location is not None:
        print("Геолокация получена")
        bot.send_message(message.chat.id, "Чтобы узнать погоду нажмите кнопку 'Узнать погоду'", reply_markup=ask_weather())
        weather = Weather(message.location.longitude, message.location.latitude)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    print(f"Получено сообщение: {message.text}")
    if message.text.lower() in ["погода", "дай погоду", "какая погода", "узнать погоду"]:
        if weather:
            bot.send_message(message.chat.id, weather.get_weather())
        else:
            bot.send_message(message.chat.id, "Вы не указали своё местоположение и я не могу сказать вам погоду(", reply_markup=ask_geo())
    elif message.text.lower() in ["сменить местоположение", "другое место", "изменить местоположение"]:
        bot.send_message(message.chat.id, "Укажите другое местоположение", reply_markup=ask_geo())
    else:
        bot.send_message(message.chat.id, "Я пока что не знаю такой команды")

bot.polling(none_stop=True, interval=0)
