# fish
# virtualenv venv
# source venv/bin/activate.fish
# pip install requests
# pip install python-dotenv
# pip freeze > requirements.txt
# Переключить интерпритатор

import json
import requests
from pprint import pprint
from os import getenv, system
from dotenv import load_dotenv
load_dotenv()


USER_URL = getenv("URL")


def get_request(url):
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return f"Плохой запрос: {response.status_code}"


def random_users(random_url=USER_URL):
    data = get_request(random_url)
    #with open("core/json/users.json", "w", encoding="UTF-8") as json_file:
    #    json.dump(data, json_file, indent=4, ensure_ascii=False)
    data = data['results'][0]

    Informations = f"""
    ФИО: {data['name']['title']} {data['name']['last']}
    Дата рождения: {data['dob']['age']}
    Возрас: {data['dob']['age']}
    Пол: {data['gender']}
    Национальность: {data['nat']}
    Страна: {data['location']['country']}
    Город: {data['location']['state']}
    Местоположение: {data['location']['coordinates']['latitude']}, {data['location']}


    Домашний номер: {data['phone']}
    Мобильный номер: {data['cell']}

    Электроннаяпочта: {data['email']}
    Пользовательское имя: {data['login']['username']}
    Пароль: {data['login']['password']}
    Дата регистраций аккаунта: {data['registered']['date']}
    """
    return Informations

print(random_users())


