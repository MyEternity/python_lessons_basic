'''
Есть два списка:
tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']
Необходимо реализовать генератор, возвращающий кортежи вида (<tutor>, <klass>), например:
('Иван', '9А')
('Анастасия', '7В')
Количество генерируемых кортежей не должно быть больше длины списка tutors. Если в списке klasses меньше элементов,
чем в списке tutors, необходимо вывести последние кортежи в виде: (<tutor>, None), например:
('Станислав', None)

Доказать, что вы создали именно генератор. Проверить его работу вплоть до истощения.
Подумать, в каких ситуациях генератор даст эффект.
'''


def create_students_generator(list_of_students=[], list_of_classrooms=[]):
    # Выравниваем наш список кабинетов/классов.
    while len(list_of_classrooms) < len(list_of_students):
        list_of_classrooms.append(None)
    # Наш генератор.
    for i, el in enumerate(list_of_students):
        yield list_of_students[i], list_of_classrooms[i]


tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена', 'Катя', 'Олеся']
# Ну транслит же?
# klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']
classrooms_list = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']

# Это генератор?
test_gen = create_students_generator(tutors, classrooms_list)
# Пробуем его истощить.
print(next(test_gen))
print(next(test_gen))
print(next(test_gen))
print(next(test_gen))
print(next(test_gen))
print(next(test_gen))
print(next(test_gen))
print(next(test_gen))
print(next(test_gen))
print(next(test_gen))
print(next(test_gen))
# генератор пригодится чтобы например выдавать студентов у которых есть номера классов.
# остальных можно будет уже распределять по номерам.
