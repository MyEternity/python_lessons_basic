'''
Найти IP адрес спамера и количество отправленных им запросов по данным файла логов из предыдущего задания.
Примечания: спамер — это клиент, отправивший больше всех запросов; код должен работать даже с файлами, размер
которых превышает объем ОЗУ компьютера.
'''

# Читаем файл.
with open('nginx_logs.txt') as f:
    data = (i.split(' ') for i in f.readlines())

# Собираем только нужные нам данные.
res = ((i[0], i[5].replace('"', ''), i[6]) for i in data)

count_requests = {}
for i in res:
    if not i[0] in count_requests.keys():
        count_requests[i[0]] = 1
    else:
        count_requests[i[0]] += 1

my_list = list(count_requests.items())
my_list.sort(key=lambda i: i[1])
print(f'IP Адрес спамера: {my_list[-1][0]}, запросов: {my_list[-1][1]}')
