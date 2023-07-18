
def read_command(command):
    """Функция которая обращается к файлу с sql запросами
    и возвращает нужную команду по индексу"""
    with open('queries.sql', 'r') as file:
        queries = file.readlines()

    # Удаление лишних пробелов и символов новой строки
    queries = [query.strip() for query in queries]
    return queries[command]
