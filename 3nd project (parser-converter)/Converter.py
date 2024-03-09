import json


with open('money.json') as f:
    data = json.load(f)


def ConverterVsegoAncient():
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
        ConverterVsegoAncient()


def ConverterVsego():
    money_start = input('Введите начальную валюту: ')
    money_start2 = input('Введите конечную валюту: ')
    money_start_flag = 0
    money_start2_flag = 0
    Currencies = []
    item_count = -1
    for i in data:
        Currencies.append([i['Letters. code'], i['Currency'], i['Course'], i['Units']])
        item_count += 1
        if money_start2 == Currencies[item_count][0]:
            money_start2_flag = 1
        if money_start == Currencies[item_count][0]:
            money_start_flag = 1

    if money_start == 'RUB' and money_start2_flag:
        for i in data:
            if i['Letters. code'] == money_start2:
                try:
                    money = float(input(f'Вы выбрали {i['Currency']}\nВведите деньги в Рублях: '))
                    multiply = round(money / round(float(i['Course']), 3), 3)
                    money_end = multiply * float(i['Units'])
                    print(f'{money} Рублей в {i['Currency']} будет {money_end}')
                    print('Вывод даты')
                    break
                except Exception as e:
                    print(e)
                    print('Неправильный ввод попробуйте снова')
                    break

    elif money_start_flag and money_start2_flag:
        flag = 1
        for i in data:
            if i['Letters. code'] == money_start:
                for j in range(len(Currencies)):
                    if Currencies[j][0] == money_start2:
                        try:
                            print(f'Вы выбрали перевод с {i['Currency']} в {Currencies[j][1]}')
                            money_s = int(input(f'Введите деньги в {i['Currency']} '))
                            multiply = round(money_s/int(i['Units']), 3)
                            money_end = multiply * float(i['Course'])

                            money = money_end
                            multiply = round(money / round(float(Currencies[j][2]), 3), 3)
                            money_end = round(multiply * float(Currencies[j][3]), 3)
                            print(f'{money_s} {i['Currency']} в {Currencies[j][1]} будет {money_end}')
                            print('Вывод даты')
                            flag = 0
                            break

                        except Exception as e:
                            print(e)
                            print('Неправильный ввод попробуйте снова')
                            flag = 0
                            break
            if flag == 0:
                break
    elif money_start2 == 'RUB' and money_start_flag:
        for i in data:
            if i['Letters. code'] == money_start:
                try:
                    money = int(input(f'Введите деньги в {i['Currency']} '))
                    multiply = round(money/int(i['Units']), 3)
                    money_end = multiply * float(i['Course'])
                    print(f'{money} {i['Currency']} в рублях будет {money_end}')
                    print('Вывод даты')
                    break
                except Exception as e:
                    print(e)
                    print('Неправильный ввод попробуйте снова')
                    break


    else:
        print('Неверный ввод, повторите попытку')
        ConverterVsego()


def ConverterTelebot(money_start, money, money_start2,):
    money_start_flag = 0
    money_start2_flag = 0
    Currencies = []
    item_count = -1
    for i in data:
        Currencies.append([i['Letters. code'], i['Currency'], i['Course'], i['Units']])
        item_count += 1
        if money_start2 == Currencies[item_count][0]:
            money_start2_flag = 1
        if money_start == Currencies[item_count][0]:
            money_start_flag = 1

    if money_start == 'RUB' and money_start2_flag:
        flag_tg = 1
        items = []
        for i in data:
            if i['Letters. code'] == money_start2:
                try:
                    # money = money  # Ввод валюты, i['Currency'] передадим в return для вывода в тг боте
                    money = float(money)
                    multiply = round(money / round(float(i['Course']), 3), 3)
                    money_end = multiply * float(i['Units'])  # Вывод
                    items.extend([i['Currency'], money, money_end, flag_tg])
                    return items
                except Exception as e:
                    print(e)
                    print('Неправильный ввод попробуйте снова')
                    flag_tg = 0
                    items.extend([i['Currency'], money, 0, flag_tg])
                    return items


    elif money_start2 == 'RUB' and money_start_flag:
        flag_tg = 1
        items = []
        for i in data:
            if i['Letters. code'] == money_start:
                try:
                    money = float(money)
                    multiply = round(money/int(i['Units']), 3)
                    money_end = multiply * float(i['Course'])
                    items.extend([i['Currency'], money, money_end, flag_tg])
                    return items
                except Exception as e:
                    print(e)
                    print('Неправильный ввод попробуйте снова')
                    flag_tg = 0
                    items.extend([i['Currency'], money, 0, flag_tg])
                    return items

    elif money_start_flag and money_start2_flag:
        flag_tg = 1
        items = []
        for i in data:
            if i['Letters. code'] == money_start:
                for j in range(len(Currencies)):
                    if Currencies[j][0] == money_start2:
                        try:
                            money_s = float(money)
                            multiply = round(money_s/int(i['Units']), 3)
                            money_end = multiply * float(i['Course'])

                            money = money_end
                            multiply = round(money / round(float(Currencies[j][2]), 3), 3)
                            money_end = round(multiply * float(Currencies[j][3]), 3)

                            # Передаём i['Currency'], money_s, money_end, flag_tg, Currencies[j][1]
                            items.extend([i['Currency'], money_s, money_end, flag_tg, Currencies[j][1]])
                            return items

                        except Exception as e:
                            print(e)
                            print('Неправильный ввод попробуйте снова')
                            flag_tg = 0
                            items.extend([i['Currency'], 0, 0, flag_tg, Currencies[j][1]])
                            return items


if __name__ == "__main__":
    if input('Старый/Новый y/n: ') == 'y':
        ConverterVsegoAncient()
    else:
        print('Значит новый')
        ConverterVsego()

else:
    print('Осуществляеться ConverterTelebot()')