'''
Реализовать базовый класс Worker (работник):
определить атрибуты: name, surname, position (должность), income (доход);

последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы «оклад» и «премия»,
например, {"wage": wage, "bonus": bonus};

создать класс Position (должность) на базе класса Worker;
в классе Position реализовать методы получения полного имени сотрудника (get_full_name) и
    дохода с учётом премии (get_total_income);
проверить работу примера на реальных данных: создать экземпляры класса Position,
передать данные, проверить значения атрибутов, вызвать методы экземпляров.
'''


class Worker():
    # Создание класса.
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        # Проверка на корректность значения
        if type(income) is dict:
            self.__income = income

    # Для получения защищенного атрибута.
    def full_income(self):
        try:
            return self.__income['wage'] + self.__income['bonus']
        except:
            return 0


# Штатная единица.
class Position(Worker):
    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return f'Доход с учетом премии: {self.full_income()}'


# Тестируем.
p1 = Position('Василий', 'Петров', 'Сварщик', {"wage": 35000, "bonus": 15000})
print(p1.get_full_name())
print(p1.get_total_income())
