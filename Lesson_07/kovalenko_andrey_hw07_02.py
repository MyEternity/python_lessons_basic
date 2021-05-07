'''
Написать скрипт, создающий из config.yaml стартер для проекта со следующей структурой:

|--my_project
   |--settings
   |  |--__init__.py
   |  |--dev.py
   |  |--prod.py
   |--mainapp
   |  |--__init__.py
   |  |--models.py
   |  |--views.py
   |  |--templates
   |     |--mainapp
   |        |--base.html
   |        |--index.html
   |--authapp
   |  |--__init__.py
   |  |--models.py
   |  |--views.py
   |  |--templates
   |     |--authapp
   |        |--base.html
   |        |--index.html

Примечание: структуру файла config.yaml придумайте сами, его можно создать в любом текстовом редакторе «руками»
(не программно); предусмотреть возможные исключительные ситуации, библиотеки использовать нельзя.
'''

import routines

# Прибираем мусор.
routines.process_path('config_clean_trash.yaml')
# Весь код в routines.
routines.process_path('config_l2.yaml')
