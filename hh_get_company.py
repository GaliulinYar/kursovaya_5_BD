import requests


def connect_vacancy(id_company):
    """функция подключения к хх ру и получения json файла"""

    url = 'https://api.hh.ru/vacancies'
    params = {'employer_id': id_company,
              'per_page': '100'}
    headers = {
        "User-Agent": "50355527",  # User-Agent header взятый из личного кабинета хх ру
    }

    response = requests.get(url, params=params, headers=headers)  # Реализация подключения к API hh.ru

    if response.status_code == 200:
        data = response.json()

        return data
    #  обработка ошибки
    else:
        print(f'Ой, что- то пошло нет так, код ответа{response.status_code}')
