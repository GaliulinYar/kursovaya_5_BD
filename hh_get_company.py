# import json
# from abc import ABC
from pprint import pprint
import psycopg2
import requests
# from utils.abstract_class import AbstractJobPlatform

# 'open_vacancies' - ключ для кол-ва вакансий

count = [9498112, 3529, 78638]

def connect_vacancy(id_company):
    # Реализация подключения к API hh.ru

    url = 'https://api.hh.ru/vacancies'
    params = {'employer_id': id_company,
              'per_page': '100'}
    headers = {
        "User-Agent": "50355527",  # User-Agent header взятый из личного кабинета хх ру
    }

    response = requests.get(url, params=params, headers=headers)

    if response.status_code == 200:
        data = response.json()

    return data


pprint(connect_vacancy(78638))

conn = psycopg2.connect(host='localhost', database='north', user='postgres', password='qwerty')  # Данные БД
cur = conn.cursor()  # Включение курсора
cur.execute("""SELECT company_name FROM customers WHERE company_name LIKE '%v%'""")
rows = cur.fetchall()

cur.close()  # Закрываем курсор
conn.close()  # Закрываем подключение к БД
for i in rows:
    print(i[0])

