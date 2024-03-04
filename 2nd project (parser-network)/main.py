import requests
from bs4 import BeautifulSoup
import json

""" # Все адреса персонала в txt файл
def Personal():
    persons_user_url = []
    for i in range(0, 760, 12):
        url = f'https://www.bundestag.de/ajax/filterlist/en/members/863330-863330?limit=12&noFilterSet=true&offset={i}'
    
        link = requests.get(url)
        result = link.content
    
        soup = BeautifulSoup(result, features='lxml')
    
        persons = soup.find_all(class_='bt-slide-content')
    
        for person in persons:
            per = person.find_next().get('href')
            persons_user_url.append(per)
    
    
    with open('persons.txt', 'w') as file:
        for links in persons_user_url:
            file.write(f'{links}\n')
"""

def main():
    with open('persons.txt', 'r') as file:

        lines = [line.strip() for line in file.readlines()]

        count = 0
        data_dict = []
        for url in lines:    # Нельзя делать for url in file.readlines() Ибо чтение soup'a будет не верным

            link = requests.get(url)
            result = link.content

            soup = BeautifulSoup(result, features='lxml')

            # Вытащим Имя и работу
            person_name_and_job = soup.find(class_='bt-biografie-name').find('h3').text
            person_name_and_job_array = person_name_and_job.strip().split(',')

            person_name = person_name_and_job_array[0]
            person_job = person_name_and_job_array[1].strip()

            # print('\n', person_name,'\n', person_job)

            # Вытпщим ссылки на соц страницы

            Web = soup.find_all(class_='bt-link-extern')
            Web_urls = []
            for item in Web:
                Web_urls.append(item.get('href'))

            data = {
                'person_name': person_name,
                'person_job': person_job,
                'Web_urls': Web_urls,
            }

            data_dict.append(data)

            with open('persons.json', 'w') as json_file:
                json.dump(data_dict, json_file, indent=4)

            count += 1
            print(f'{count} Персона загружена успешно!')


if __name__ == '__main__':
    # Personal()
    main()
    pass