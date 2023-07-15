import psycopg2
from config import config

# params1 = config()


def create_database():
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
        company_id int,
        salary_from int,
        salary_to int,
        url text)""")
    conn.commit()
    conn.close()
    print('Базу и таблицы создали')


def write_table(data_list, company_id):

    # vac['name']
    #     vac['salary']
    #     vac['salary']['from']
    #     vac['salary']['to']
    # company_id
    # vac['alternate_url']
    # vac['items'][0]['employer']['name']

    #corteg_for_table = (company_id, data_list['items'][0]['employer']['name'], data_list['found'])
    #print(corteg_for_table)

    conn = psycopg2.connect(host='localhost', database='database_hhru', user='postgres', password='qwerty', port=5432)  # Данные БД

    cur = conn.cursor()  # Включение курсора
    corteg_for_table = (company_id, data_list['items'][0]['employer']['name'], data_list['found'])
    cur.execute('INSERT INTO company_info VALUES (%s, %s, %s)', corteg_for_table)  # Добавление списка кортежей в таблицы



        # cur.executemany('INSERT INTO customers VALUES (%s, %s, %s)', list_from_customers_data[1:])  # Добавление списка кортежей в таблицы
        # cur.executemany('INSERT INTO orders VALUES (%s, %s, %s, %s, %s)', list_from_orders_data[1:])  # Добавление списка кортежей в таблицы
        #
        # cur.execute("""SELECT company_name FROM customers WHERE company_name LIKE '%v%'""")

    conn.commit()
    cur.close()  # Закрываем курсор
    conn.close()  # Закрываем подключение к БД

