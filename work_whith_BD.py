import psycopg2
from read_command_db import read_command


def create_database():
    """фугкция создание новой БД и таблиц с заголовками"""
    conn = psycopg2.connect(host='localhost', user='postgres', password='qwerty', port=5432)
    conn.autocommit = True
    cur = conn.cursor()

    cur.execute("DROP DATABASE IF EXISTS database_hhru")
    cur.execute(f'CREATE DATABASE database_hhru')
    cur.close()
    conn.close()

    conn = psycopg2.connect(host='localhost', database='database_hhru', user='postgres', password='qwerty', port=5432)
    with conn.cursor() as cur:
        cur.execute("""
            CREATE TABLE company_info (
            company_id int PRIMARY KEY,
            company_name varchar(255),
            count_vacancy int
        )""")

    with conn.cursor() as cur:
        cur.execute("""
        CREATE TABLE vacancies (
        vacancy_name varchar(255),
        company_id int REFERENCES company_info(company_id),
        salary_from int,
        salary_to int,
        url text)""")
    conn.commit()
    conn.close()
    print('Базу и таблицы создали')


def write_table(data_list, company_id):
    """функция заполнения таблиц в БД нужными данными"""

    conn = psycopg2.connect(host='localhost', database='database_hhru', user='postgres', password='qwerty', port=5432)  # Данные БД

    cur = conn.cursor()  # Включение курсора
    corteg_for_table = (company_id, data_list['items'][0]['employer']['name'], data_list['found'])
    cur.execute(read_command(0), corteg_for_table)  # Добавление списка кортежей в таблицы

    for data in data_list['items']:  # перебираем список вакансий

        vacancy_name = data['name']
        if data['salary'] is None:
            salary_from = 0
            salary_to = 0
        else:
            if data['salary']['from'] is None:
                salary_from = 0
            else:
                salary_from = data['salary']['from']

            if data['salary']['to'] is None:
                salary_to = 0
            else:
                salary_to = data['salary']['to']
        url = data['alternate_url']

        corteg_for_table2 = (vacancy_name, company_id, salary_from, salary_to, url)  # создаем кортеж для загрузки в таблицу
        cur.execute(read_command(1), corteg_for_table2)

    conn.commit()
    cur.close()  # Закрываем курсор
    conn.close()  # Закрываем подключение к БД
