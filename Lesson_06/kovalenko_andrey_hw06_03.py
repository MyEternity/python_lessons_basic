"""
Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом — данные об их хобби.
Известно, что при хранении данных используется принцип: одна строка — один пользователь, разделитель между значениями —
запятая. Написать код, загружающий данные из обоих файлов и формирующий из них словарь: ключи — ФИО,
значения — данные о хобби. Сохранить словарь в файл. Проверить сохранённые данные.
Если в файле, хранящем данные о хобби, меньше записей, чем в файле с ФИО, задаём в словаре значение None.
Если наоборот — выходим из скрипта с кодом «1».
При решении задачи считать, что объём данных в файлах во много раз меньше объема ОЗУ.

Фрагмент файла с данными о пользователях (users.csv):
Иванов,Иван,Иванович
Петров,Петр,Петрович

Фрагмент файла с данными о хобби (hobby.csv):
скалолазание,охота
горные лыжи
"""

import json
import os


# Тут мы будем собирать наш словарь.
def my_dictionary(users, hobby):
    result_dict = {}
    # Задача говорит что списки - маленькие, распакуем генераторы.
    user_list = list(users)
    hobby_list = list(hobby)
    if len(hobby_list) > len(user_list):
        raise ValueError
    # Выравниваем меньший список.
    while len(hobby_list) < len(user_list):
        hobby_list.append(None)
    # Конструируем словарь.
    for i, el in enumerate(user_list):
        result_dict[el] = hobby_list[i]
    return result_dict


# Читаем данные из файлов.
with open('users.csv', encoding='UTF8') as f:
    # Пользователи разделены символом ","
    users_data = (' '.join(i.split(',')).rstrip() for i in f.readlines())

with open('hobby.csv', encoding='UTF8') as f:
    hobby_data = (i.rstrip() for i in f.readlines())

# Получим словарь
my_dict = my_dictionary(users_data, hobby_data)

# Покажем данные нашего словаря.
print(my_dict)

# Сохраним данные словаря.
with open('saved_data.dat', 'w+') as f:
    json.dump(my_dict, f)

# Прочитаем наш словарь
my_dict = {}
with open('saved_data.dat') as f:
    print(json.load(f))

# Приберемя за собой.
if os.path.isfile('saved_data.dat'):
    os.remove('saved_data.dat')
