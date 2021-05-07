'''
Реализовать простую систему хранения данных о суммах продаж булочной.
Должно быть два скрипта с интерфейсом командной строки: для записи данных и для вывода на экран записанных данных.
При записи передавать из командной строки значение суммы продаж.
Для чтения данных реализовать в командной строке следующую логику:

 просто запуск скрипта — выводить все записи;
 запуск скрипта с одним параметром-числом — выводить все записи с номера, равного этому числу, до конца;
 запуск скрипта с двумя числами — выводить записи, начиная с номера, равного первому числу, по номер,
равный второму числу, включительно.

Подумать, как избежать чтения всего файла при реализации второго и третьего случаев.
Данные хранить в файле bakery.csv в кодировке utf-8. Нумерация записей начинается с 1. Примеры запуска скриптов:

python add_sale.py 5978,5
python add_sale.py 8914,3
python add_sale.py 7879,1
python add_sale.py 1573,7
python show_sales.py
5978,5
8914,3
7879,1
1573,7
python show_sales.py 3
7879,1
1573,7
python show_sales.py 1 3
5978,5
8914,3
7879,1
'''

import sys

from routines import *


# Проверяем и нормализуем границы, которые вводит нам пользователь.
def correct_ranges(rb='', re=''):
    # Проверим на числа.
    if rb.isdigit():
        rb = int(rb)
    else:
        rb = 0
    if re.isdigit():
        re = int(re)
    else:
        re = -1
    # Крутим - вертим границы.
    if rb - 1 <= 0:
        rb = 0
    else:
        rb = rb - 1
    if re != -1:
        re = rb + re
    return [rb, re]


# Проверяем на командную строку
if __name__ == "__main__":
    if len(sys.argv) > 2:
        offset_b = sys.argv[1]
        offset_e = sys.argv[2]
    elif len(sys.argv) > 1:
        offset_b = sys.argv[1]
        offset_e = '#'
    else:
        offset_b = '#'
        offset_e = '#'
else:
    offset_b = '#'
    offset_e = '#'

ranges = correct_ranges(offset_b, offset_e)

with open(get_database_file(), mode='r', encoding='UTF8') as f:
    records = ((r.lstrip().rstrip().replace(chr(0), '')) for r in f.readlines())
    # Тут у нас читается ВЕСЬ файл.
    # Чтобы этого избежать - можно определить длину генератора, и выбрать из него только
    # нужные нам значения, обнуляя ненужные методом next.
    result_set = list(records)
    if ranges[1] == -1:
        # тут пришлось делать вилку, т.к. срез не берет последний элемент.
        print('\n'.join(result_set[ranges[0]::]))
    else:
        print('\n'.join(result_set[ranges[0]:ranges[1]:]))
