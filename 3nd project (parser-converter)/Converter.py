import json


with open('money.json') as f:
    data = json.load(f)


def ConverterVsego():
    kakoi_perevod = input('Введите какой перевод хотите: PUB/INO ')

    if kakoi_perevod == 'PUB':
        money_start = input('Введите интересующую валюту: ')
        for i in data:
            if i['Letters. code'] == money_start:
                money = float(input(f'Вы выбрали {i['Currency']}\nВведите деньги в Рублях: '))
                multiply = round(money / round(float(i['Course'])), 3)
                money_end = multiply * float(i['Units'])
                print(f'{money} Рублей в {i['Currency']} будет {money_end}')
                break

    elif kakoi_perevod == 'INO':
        money_start = input('Введите интересующую валюту: ')
        for i in data:
            if i['Letters. code'] == money_start:
                money = int(input(f'Введите деньги в {i['Currency']} '))
                multiply = round(money/int(i['Units']), 3)
                money_end = multiply * float(i['Course'])
                print(f'{money} {i['Currency']} в рублях будет {money_end}')
                break

    else:
        print('Неверный ввод, повторите попытку:')
        ConverterVsego()

ConverterVsego()