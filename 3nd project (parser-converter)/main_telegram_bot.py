import telebot               # Отключить работу venv ctrl + c, ctrl + z
from config import token
from telebot import types
from Converter import ConverterTelebot
import random
import time

bot = telebot.TeleBot(token)

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
    bot.send_message(message.chat.id, "Привет! Я могу конвертировать валюты."
                                      " Введите Начальную валюту, Сумму начальной валюты, Конечную валюту\n"
                                      "Например: RUB 1000 KRW")


@bot.message_handler()
def momentom_v_converter(message):
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
    elif money_start2 == "RUB":
        bot.send_message(message.chat.id, f'{items[1]} {items[0]} в Рублях будет {items[2]}')
    else:
        bot.send_message(message.chat.id, f'{items[1]} {items[0]} в {items[4]} будет {items[2]}')


if __name__ == "__main__":
    Komplimenti = ['Самая Прекрасная', 'Великолепна', 'Волшебна', 'Лучшая', 'Самая Красивая']
    bot.infinity_polling()
