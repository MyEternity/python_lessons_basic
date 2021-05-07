'''
Решить задачу 4 и реализовать интерфейс командной строки, чтобы можно было задать путь к обоим исходным файлам и путь к
выходному файлу со словарём. Проверить работу скрипта для случая, когда все файлы находятся в разных папках.
'''

from routines import *

files_list = []
# Соберем первичную информацию.
files_list.append(input('Укажите путь к файлу с пользователями...'))
files_list.append(input('Укажите путь к файлу с увлечениями...'))
files_list.append(input('Укажите файл, куда нужно сохранить данные...'))
# Проверим, что нам ввели.
for i, el in enumerate(files_list):
    if not os.path.isfile(el) and i != 2:
        print(f'Странный файл: {el}!')
        raise IOError

# Построим наш словарь.
my_dictionary_ext(files_list[0], files_list[1], files_list[2], False)

# Прочитаем наш словарь
with open(files_list[2]) as f:
    print(json.load(f))

# Приберемя за собой.
if os.path.isfile(files_list[2]):
    os.remove(files_list[2])
