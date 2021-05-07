'''
Написать скрипт, который выводит статистику для заданной папки в виде словаря, в котором ключи те же, а значения —
кортежи вида (<files_quantity>, [<files_extensions_list>]), например:
  {
      100: (15, ['txt']),
      1000: (3, ['py', 'txt']),
      10000: (7, ['html', 'css']),
      100000: (2, ['png', 'jpg'])
    }
Сохраните результаты в файл <folder_name>_summary.json в той же папке, где запустили скрипт.
'''
import json

import routines

folder_name = '..\\'
my_dict = {}
cached_list = routines.folder_stat(folder_name)

for i in cached_list:
    # творим аццкую мааагию :)
    my_dict[i[2]] = sum(1 for x, y, z in cached_list if i[2] == z), list(
        set((x.split('.')[1] for x, y, z in cached_list if i[2] == z)))

# Пишем в файл.
with open('summary.json', 'w') as f:
    json.dump(my_dict, f)
