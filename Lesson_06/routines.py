import json
import os
import uuid


# Тут мы будем собирать наш словарь.
def my_dictionary_ext(users_file, hobbys_file, results_file='', keep_clean=True):
    result_dict = {}
    # Получим длины наших генераторов.
    with open(users_file, encoding='UTF8') as f:
        users_len = sum(1 for _ in f.readlines())
    with open(hobbys_file, encoding='UTF8') as f:
        hobbys_len = sum(1 for _ in f.readlines())

    if users_len < hobbys_len:
        raise ValueError

    # Читаем данные из файлов.
    with open(users_file, encoding='UTF8') as f:
        # Пользователи разделены символом ","
        users_data = (' '.join(i.split(',')).rstrip() for i in f.readlines())

    with open(hobbys_file, encoding='UTF8') as f:
        hobby_data = (i.rstrip() for i in f.readlines())

    # Создаем словарь, где у каждой записи будет свой UUID.
    # С точки зрения экономии памяти - можно вообще сразу писать получаемые данные в файл
    # и дальше работать с генератором из него.
    for i in range(0, users_len):
        user_line = next(users_data)
        if i < hobbys_len:
            hobby_line = next(hobby_data)
        else:
            hobby_line = None
        # Вместо гуида - можно использовать любой другой тип данных, в т.ч. и итератор.
        uid = str(uuid.uuid1())
        result_dict[uid] = {}
        result_dict[uid]['fn'] = user_line.split()[0]
        result_dict[uid]['ln'] = user_line.split()[1]
        result_dict[uid]['mn'] = user_line.split()[2]
        result_dict[uid]['hh'] = hobby_line

    # задел на будущее - будем сохранять наш словарь.
    if len(result_dict) >= 1:
        with open(results_file, 'w+') as f:
            json.dump(result_dict, f)

    # Приберемя за собой если нас об этом попросили.
    if os.path.isfile(results_file) and keep_clean:
        os.remove(results_file)

    # Ну и вернем наш словарь.
    return result_dict


# Проверка на тип Float.
def isfloat(value):
    try:
        float(value)
        if len(value) > 24:
            print('Такую космическую сумму в булочной заработать невозможно!')
            return False
        return True
    except ValueError:
        return False


# Хранить будем всегда 32 символа - для булочной даже избыточно.
def normalize_write(input_string):
    while len(input_string) < 30:
        input_string = input_string + chr(0)
    input_string = input_string + chr(13)
    return input_string


# Путь до файла с БД - зависим от каталога где запустили скрипт.
def get_database_file():
    database = os.getcwd()
    if database[-1] != '\\':
        database = database + '\\'
    database = database + 'bakery.csv'
    return database
