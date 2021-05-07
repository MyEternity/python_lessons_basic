import os
import shutil


def process_datafile(file_name='config_l1.yaml'):
    if os.path.isfile(file_name):
        with open(file_name, mode='r', encoding='UTF8') as f:
            # Первая колонка = ТИП
            # Вид операции - m move, d delete, c create.
            # Третья колонка - родитель
            # Четвертая колонка - элемент.
            # Легко и просто масштабируем наш файл до всех нужных флагов.
            file_data = (i.rstrip().lstrip().split(';') for i in f.readlines() if i[0] != '#')
        return file_data
    else:
        print(f'Не найден указанный файл конфигурации: {file_name}')
        return iter('e')


# Создание каталога.
def create_dir_path(parent_dir='', target_dir=''):
    try:
        # У нас есть родительская директория, значит создаем в т.ч. и ее
        if len(parent_dir) >= 1 and len(target_dir) >= 1:
            # Проверим, что путь до родителя соержит \
            if parent_dir[-1] != '\\':
                parent_dir = parent_dir + '\\'
            os.mkdir(parent_dir + target_dir)
        else:
            # У нас только дочерняя или корневая директория.
            if len(target_dir) >= 1:
                os.mkdir(target_dir)
    except FileExistsError:
        print(f'Каталог {parent_dir + target_dir} уже существует. Пропускаем.')


# Создание файла.
def create_file_path(parent_dir='', file_name=''):
    if len(parent_dir) >= 1:
        # Проверим, что путь до родителя содержит \
        if parent_dir[-1] != '\\':
            parent_dir = parent_dir + '\\'
        if not os.path.isfile(parent_dir + file_name):
            f = open(parent_dir + file_name, 'w')
            f.close()
        else:
            print(f'Файл {parent_dir + file_name} уже существует. Пропускаем.')


# Проходит по геренератору и создает каталог/файл по каждому итератору.
def process_path(settings_file='config_l1.yaml'):
    for i in process_datafile(settings_file):
        if i[0].lower() == 'd' and i[1].lower() == 'c':
            create_dir_path(i[2], i[3])
        if i[0].lower() == 'f' and i[1].lower() == 'c':
            create_file_path(i[2], i[3])
        if i[0].lower() == 'd' and i[1].lower() == 'd':
            shutil.rmtree(i[2], True)


def size_limit(size):
    if size <= 100:
        return 100
    elif 1000 >= size >= 101:
        return 1000
    elif 10000 >= size >= 1001:
        return 10000
    else:
        return 100000


def concat_func(path, fname):
    # Получаем данные по файлам.
    files_data = list(path + '\\' + f for f in fname if len(f) > 0)
    return list((os.path.basename(fn), os.stat(fn).st_size, size_limit(os.stat(fn).st_size)) for fn in files_data)


# Получает данные по директории.
def folder_stat(folder_path='d:\\Distrib\\IBEXPERT'):
    result_set = []
    # Смотрим ТОЛЬКО файлы.
    folder_data = (concat_func(dir_path, file_names) for dir_path, dir_names, file_names in os.walk(folder_path) if
                   len(file_names) > 0)
    # И тут у нас списки из кортежей. Сольем их в один общий список.
    for i in folder_data:
        for x in i:
            result_set.append([x[0], x[1], x[2]])
    return result_set
