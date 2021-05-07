'''
Добавить возможность редактирования данных при помощи отдельного скрипта: передаём ему номер записи и новое значение.
При этом файл не должен читаться целиком — обязательное требование.
Предусмотреть ситуацию, когда пользователь вводит номер записи, которой не существует.
'''

from routines import *

# Так как у нас файл содержит четко 32 символа в строке
# Создадим генератор, чтобы определить длину файла.
with open(get_database_file(), mode='r', encoding='UTF8') as f:
    records_count = sum(1 for _ in f.readlines())

# Все наши проверки здесь.
record_num = input('Введите номер записи, которую нужно изменить: \n')
if not record_num.isdigit():
    print('Номер записи - это целое число.')
    raise SyntaxError
else:
    record_num = int(record_num)

if record_num > records_count:
    print('Записи с таким номером не существует!')
    raise LookupError

record_data = input('Введите новую сумму: \n')
if not isfloat(record_data):
    print('Некорректное значение. Сумма должна быть целым/дробным числом!')
    raise SyntaxError

# И волшебство записи - крайне простое
# Спускаемся на нужный нам номер строки (мы выше проверили же - что он есть)
# и спокойно пишем наши данные.
with open(get_database_file(), mode='r+', encoding='UTF8') as f:
    f.seek((record_num - 1) * 31)
    f.writelines(normalize_write(record_data))
