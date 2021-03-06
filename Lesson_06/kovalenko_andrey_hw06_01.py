"""
Не используя библиотеки для парсинга, распарсить (получить определённые данные) файл логов web-сервера nginx_logs.txt.txt
(https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs) —
    получить список кортежей вида: (<remote_addr>, <request_type>, <requested_resource>).

Например:
[
...
('141.138.90.60', 'GET', '/downloads/product_2'),
('141.138.90.60', 'GET', '/downloads/product_2'),
('173.255.199.22', 'GET', '/downloads/product_2'),
...
]
Примечание: код должен работать даже с файлами, размер которых превышает объем ОЗУ компьютера.
"""

# Читаем файл.
with open('nginx_logs.txt') as f:
    data = (i.split(' ') for i in f.readlines())

# Собираем только нужные нам данные.
res = ((i[0], i[5].replace('"', ''), i[6]) for i in data)

# результат
print(next(res))
print(next(res))
print(next(res))
print(next(res))
