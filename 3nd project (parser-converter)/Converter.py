import json


with open('money.json') as f:
    data = json.load(f)


def ConverterVsego():
    kakoi_perevod = input('Введите какой перевод хотите: PUB/INO ')

    if kakoi_perevod == 'PUB':
        money_start = input('Введите интересующую валюту: ')
        for i in data:
            if i['Letters. code'] == money_start:
                try:
                    money = float(input(f'Вы выбрали {i['Currency']}\nВведите деньги в Рублях: '))
                    multiply = round(money / round(float(i['Course']), 3), 3)
                    money_end = multiply * float(i['Units'])
                    print(f'{money} Рублей в {i['Currency']} будет {money_end}')
                    print('data')
                    break
                except Exception as e:
                    print(e)
                    print('Неправильный ввод попробуйте снова')
                    break
        else:
            print('Извините, такой валюты нет')

    elif kakoi_perevod == 'INO':
        money_start = input('Введите интересующую валюту: ')
        for i in data:
            if i['Letters. code'] == money_start:
                try:
                    money = int(input(f'Введите деньги в {i['Currency']} '))
                    multiply = round(money/int(i['Units']), 3)
                    money_end = multiply * float(i['Course'])
                    print(f'{money} {i['Currency']} в рублях будет {money_end}')
                    print('data')
                    break
                except Exception as e:
                    print(e)
                    print('Неправильный ввод попробуйте снова')
                    break
        else:
            print('Извините, такой валюты нет')

    else:
        print('Неверный ввод, повторите попытку:')
        ConverterVsego()

ConverterVsego()