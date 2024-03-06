from bs4 import BeautifulSoup
import requests
import json


def main():
    # datatime =  Можем записать дату и передавать в url
    url = 'https://cbr.ru/currency_base/daily/'

    link = requests.get(url)
    result = link.content

    soup = BeautifulSoup(result, features='lxml')
    money = soup.find_all('td')

    money_data = []  # Конечное
    data = []  # Вся инфа

    for item in money:
        data.append(item.text)

    for count in range(0, len(data), 5):
        data[count+4] = data[count+4].replace(",", ".")
        money_dict = {
            'Digits. code': data[count],
            'Letters. code': data[count+1],
            'Units': data[count+2],
            'Currency': data[count+3],
            'Course': data[count+4]
        }
        money_data.append(money_dict)

    with open('money.json', 'w') as json_file:
        json.dump(money_data, json_file, indent=4)


if __name__ == '__main__':
    main()

