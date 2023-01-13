from telebot import types


def ask_geo():
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_geo = types.KeyboardButton(text="Отправить местоположение", request_location=True)
    keyboard.add(button_geo)
    return keyboard

def ask_weather():
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button = types.KeyboardButton(text="Узнать погоду")
    button1 = types.KeyboardButton(text="Изменить местоположение")
    keyboard.add(button, button1)
    return keyboard