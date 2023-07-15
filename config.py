from configparser import ConfigParser


def config(filename="database.ini", section="postgresql"):
    # create a parser, сбор параметров из файла database
    parser = ConfigParser()
    # read config file, читаем параметры
    parser.read(filename)
    db = {}  # Создается словарь с параметрами
    if parser.has_section(section):  # Заполнение параметров
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception(
            'Section {0} is not found in the {1} file.'.format(section, filename))
    return db
