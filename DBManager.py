import psycopg2

from read_command_db import read_command


class DBManager:

    def __init__(self, params: dict):
        self.params = params

    def get_companies_and_vacancies_count(self):
        """получает список всех компаний и количество вакансий у каждой компании."""
        conn = psycopg2.connect(database='database_hhru', **self.params)
        with conn.cursor() as cur:
            cur.execute(read_command(2))
            rows = cur.fetchall()
            for row in rows:
                print(f'Компании - {row[0]} \ всего вакансий {row[1]}')

    def get_all_vacancies(self):
        """получает список всех вакансий с указанием названия компании, названия вакансии и зарплаты и ссылки на вакансию"""
        conn = psycopg2.connect(database='database_hhru', **self.params)
        with conn.cursor() as cur:
            cur.execute(read_command(3))
            rows = cur.fetchall()
            for row in rows:
                print(
                    f'Компания - {row[0]} \ Вакансия - {row[1]} \ ЗП от - {row[2]} \ ЗП до - {row[3]} \ссылка - {row[4]}')

    def get_avg_salary(self):
        """получает среднюю зарплату по вакансиям в кампаниях"""
        conn = psycopg2.connect(database='database_hhru', **self.params)
        with conn.cursor() as cur:
            cur.execute(read_command(4))
            rows = cur.fetchall()
            for row in rows:
                print(f'Компания - {row[0]} \ Средняя ЗП - {row[1]}')

    def get_vacancies_with_higher_salary(self):
        """получает список и ссылку всех вакансий,у которых зп выше средней по всем вакансиям."""
        conn = psycopg2.connect(database='database_hhru', **self.params)
        with conn.cursor() as cur:
            cur.execute(read_command(5))
            rows = cur.fetchall()
            for row in rows:
                print(f'Вакансия - {row[0]} \ Ссылка- {row[1]}')

    def get_vacancies_with_keyword(self):
        """получает список  и ссылку всех вакансий, в названии которых
        содержатся переданные в метод слова, например “python”."""
        conn = psycopg2.connect(database='database_hhru', **self.params)
        with conn.cursor() as cur:
            cur.execute(read_command(6))
            rows = cur.fetchall()
            for row in rows:
                print(f'Вакансия - {row[0]} \ Ссылка- {row[1]}')
