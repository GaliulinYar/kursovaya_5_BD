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
            number_of_vacancies int
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
    print('типа создали')

create_database()