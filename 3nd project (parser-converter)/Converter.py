import json


with open('money.json') as f:
    data = json.load(f)


money_start = input('Введите интересующую валюту: ')
for i in data:
    if i['Letters. code'] == money_start:
        money = int(input(f'Введите деньги в {i['Currency']} '))
        multiply = round(money/int(i['Units']), 3)
        money_end = multiply * float(i['Course'])
        print(f'{money} {i['Currency']} в рублях будет {money_end}')
        break

