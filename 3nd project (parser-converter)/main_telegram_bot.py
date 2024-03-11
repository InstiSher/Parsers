import telebot               # Отключить работу venv ctrl + c, ctrl + z
from config import token
from telebot import types
from Converter import ConverterTelebot
import random
import time
import json

bot = telebot.TeleBot(token)


def units(message):
    with open('money.json') as f:
        data = json.load(f)

    with open('datatime.txt') as file:
        datatime = file.readlines()[0]
    bot.send_message(message.chat.id, text=f'Валюта, Букв.Код, Едениц к рублю')
    for i in data:
        bot.send_message(message.chat.id, text=f'{i["Currency"]}, {i["Letters. code"]}, {i["Units"]}, {i["Course"]}')
    bot.send_message(message.chat.id, text=f'Рашн Рубль, RUB\n'
                                           f'Актуальность информации: {datatime}')


@bot.message_handler(content_types=['audio', 'photo', 'sticker', 'video'])
def momentom_v_converter(message):
    print(message)
    if message.from_user.username == "Kitsune_KA" or message.from_user.username == "Ded_hurricane":
        global Komplimenti
        print('Опа Комплимент')
        bot.send_message(message.chat.id, text=f"Ты {Komplimenti[random.randint(0, 4)]}, Элина")
        time.sleep(1)
        bot.send_message(message.chat.id, text=f"Даже для Бота ❤️")


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('Существующие валюты')
    markup.add(btn1)
    bot.send_message(message.chat.id, "Привет! Я могу конвертировать валюты."
                                      " Введите Начальную валюту, Сумму начальной валюты, Конечную валюту\n"
                                      "Например: RUB 1000 KRW\n", reply_markup=markup)


@bot.message_handler()
def momentom_v_converter(message):
    if message.text == 'Существующие валюты':
        units(message)
    else:
        converter(message)


def converter(message):
    money_start = '0'
    money_start2 = '0'
    try:
        money_start, money, money_start2 = message.text.split(' ')
        items = ConverterTelebot(money_start, money, money_start2)
    except:
        items = [0, 0, 0, 0, 0]
    if not items[3]:
        bot.send_message(message.chat.id, 'Неправильный ввод попробуйте снова\n'
                                          'Введите Начальную валюту, Сумму начальной валюты, Конечную валюту\n'
                                          'Например: RUB 1000 KRW')
    elif money_start == "RUB":
        bot.send_message(message.chat.id, f'{items[1]} Рублей в {items[0]} будет {items[2]}')
        time.sleep(1)
        bot.send_message(message.chat.id, f'Не забудь ответить мне смайликом :3')
    elif money_start2 == "RUB":
        bot.send_message(message.chat.id, f'{items[1]} {items[0]} в Рублях будет {items[2]}')
        time.sleep(1)
        bot.send_message(message.chat.id, f'Не забудь ответить мне смайликом :3')
    else:
        bot.send_message(message.chat.id, f'{items[1]} {items[0]} в {items[4]} будет {items[2]}')
        time.sleep(1)
        bot.send_message(message.chat.id, f'Не забудь ответить мне смайликом :3')


if __name__ == "__main__":
    Komplimenti = ['Самая Прекрасная', 'Великолепна', 'Волшебна', 'Лучшая', 'Самая Красивая']
    bot.infinity_polling()
