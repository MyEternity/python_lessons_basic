'''
Создать структуру файлов и папок, как написано в задании 2 (при помощи скрипта или «руками» в проводнике).
Написать скрипт, который собирает все шаблоны в одну папку templates, например:

|--my_project
   ...
  |--templates
   |   |--mainapp
   |   |  |--base.html
   |   |  |--index.html
   |   |--authapp
   |      |--base.html
   |      |--index.html

Примечание: исходные файлы необходимо оставить; обратите внимание, что html-файлы расположены в родительских папках
(они играют роль пространств имён); предусмотреть возможные исключительные ситуации;
это реальная задача, которая решена, например, во фреймворке django.
'''

from routines import *

# Прибираем мусор.
process_path('config_clean_trash.yaml')
# Создадим данные по второму уроку.
process_path('config_l2.yaml')
# И наш новый каталог templates
process_path('config_l3.yaml')
# Тут у нас нет возможности работать с шаблоном, поэтому будем работать по дереву.
# Отберем только папки с шаблонами.
gen = ((dir_path, dir_names, file_names) for dir_path, dir_names, file_names in os.walk(".\my_project") if
       dir_path.split('\\')[-1] == 'templates')

task_list = list(gen)
action_list = []
target_dir = ''

# Каталог назначения.
for i in task_list:
    # Куда копируем.
    if len(i[1]) == 0:
        target_dir = i[0]

# генерируем задачу.
for i in task_list:
    if len(i[1]) > 0:
        action_list.append([target_dir + '\\' + ''.join(i[1]), i[0] + '\\' + ''.join(i[1])])

# Копируем.
for i in action_list:
    # Сказали оставить файлы... оставим.
    # По нашему сценарию - тут ошибки быть не может, т.к выше в коде
    # осуществляется генерация задачи только в том случае, если каталог назначения - пустой.
    shutil.copytree(i[1], i[0])
