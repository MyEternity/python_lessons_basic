'''
Дан список, содержащий искажённые данные с должностями и именами сотрудников:
['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
Известно, что имя сотрудника всегда в конце строки.
Сформировать из этих имён и вывести на экран фразы вида: 'Привет, Игорь!'
Подумать, как получить имена сотрудников из элементов списка, как привести их к корректному виду.
Можно ли при этом не создавать новый список?

'''

person_list = ['инженер-конструктор Игорь',
               'главный бухгалтер МАРИНА',
               'токарь высшего разряда нИКОЛАй',
               'директор аэлита']

# Сотрудник, с которым работаем.
person_name = ''

for element in person_list:
    # Имя сотрудника всегда в конце строки.
    # Чтобы не создавать новый список с именами (как переменную) - просто получаем их разделив строку
    # так-то технически, код создаст список element.split(' ')... :(
    # person_name = element.split(' ')[len(element.split(' '))-1].capitalize()
    person_name = element.split(' ')[-1].capitalize()
    # Поприветствуем наших героев!
    print(f'Привет, {person_name}!')