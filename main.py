from pprint import pprint

import requests
def connect(id_company):
    # Реализация подключения к API hh.ru

    url_hh = f"https://api.hh.ru/employers/{id_company}"
    # params = {'employer_id': id_company,
    #           'per_page': '100'}
    headers = {
        "User-Agent": "50355527",  # User-Agent header взятый из личного кабинета хх ру
    }

    response = requests.get(url_hh, headers=headers)

    if response.status_code == 200:
        list_datd = response.json()

    return list_datd

pprint(connect(3529))