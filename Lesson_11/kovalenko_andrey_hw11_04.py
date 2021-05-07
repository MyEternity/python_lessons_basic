'''
Начать работу над проектом «Склад оргтехники».
Создать класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведённых типов.
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

Разработать методы, которые отвечают за приём оргтехники на склад и передачу в определённое подразделение компании.
Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных,
    можно использовать любую подходящую структуру (например, словарь).
Реализовать механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.

Подсказка: постарайтесь реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.
'''
from abc import ABC, abstractmethod
from datetime import datetime
from uuid import uuid4


class Equipment(ABC):
    """
        Оборудование.
    """
    __types = {'p': 'Принтер', 's': 'Сканер', 'с': 'Ксерокс'}

    @abstractmethod
    def __init__(self, serial_number, eq_type):
        # Вся техника сначала приходит на главный склад.
        self.serial_number = serial_number
        self.__eq_type = self.__types.get(eq_type, 'Неизвестно')
        self.__id = uuid4()
        self.__price = 0

    @property
    def equipment_type(self):
        return self.__eq_type

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        self.__price = value

    @property
    def id(self):
        return self.__id

    def __str__(self):
        return f'Обрудование ID: {self.__id}, Тип {self.equipment_type}, Серийный номер: {self.serial_number}, ' \
               f'Цена: {self.price} руб.\n'


class WareHouse:
    """
    Склад.
    """

    def __init__(self, basement, basement_type):
        # Реквизиты склада.
        self.basement = basement
        self.basement_type = basement_type
        self.__id = uuid4()
        self.__postal_address = 'Волгоград, Ленина пр. 104 д.'
        self.__postal_code = 400117
        self.__inn = 34200010001
        self.__kpp = 342010101
        self.__rests = {}

    @property
    def id(self):
        return self.__id

    @property
    def postal_address(self):
        return self.__postal_address

    @property
    def postal_code(self):
        return self.__postal_code

    @property
    def inn(self):
        return self.__inn

    @property
    def kpp(self):
        return self.__kpp

    @postal_address.setter
    def postal_address(self, value):
        self.__postal_address = value

    @postal_code.setter
    def postal_code(self, value):
        self.__postal_code = value

    @inn.setter
    def inn(self, value):
        self.__inn = value

    @kpp.setter
    def kpp(self, value):
        self.__kpp = value

    def __str__(self):
        return f'Склад ID: {self.id}, Имя: {self.basement}, Тип: {self.basement_type}\n' \
               f'Адрес: {self.postal_code} {self.postal_address} \n' \
               f'Реквизиты: ИНН {self.inn}, КПП {self.kpp} \n' \
               f'Остатки на складе: {len(self.__rests.items())} шт. \n'

    def add_in_stock(self, unit):
        """
        Осуществляет оприходование на склада.
            :param unit: Любой из известных дочерних классов типа "Оборудование".
            :return: Ставит на остатки оборудование.
        """
        if type(unit) in (Printer, Scanner, Copier):
            if not self.__rests.get(unit.id, False):
                self.__rests[unit.id] = (datetime.now(), unit.equipment_type, unit)
                print(
                    f'Оборудование ID: {unit.id} ({unit.equipment_type}) принято на склад ID: {self.id} ({self.postal_code} {self.postal_address}).')
            else:
                print(
                    f'Оборудование ID: {unit.id} ({unit.equipment_type}) уже числится на складе ID: {self.id} ({self.postal_code} {self.postal_address}).')

    def del_from_stock(self, unit):
        """
        Осуществляет списание со склада.
            :param unit: Любой из известных дочерних классов типа "Оборудование".
            :return: Убирает с остатков оборудование.
        """
        if type(unit) in (Printer, Scanner, Copier):
            if self.__rests.get(unit.id, '') != '':
                self.__rests.pop(unit.id)
                print(
                    f'Оборудование ID: {unit.id} ({unit.equipment_type}) списано со склада ID: {self.id} ({self.postal_code} {self.postal_address}).')
            else:
                print(
                    f'Оборудование ID: {unit.id} ({unit.equipment_type}) не числится на складе ID: {self.id} ({self.postal_code} {self.postal_address}).')

    # Итератор для остатков на складе.
    def __iter__(self):
        return (el for el in self.__rests.items())


class Printer(Equipment):
    def __init__(self, serial_number):
        super().__init__(serial_number, 'p')
        self.__id = uuid4()
        self.__page_count = 10

    @property
    def page_count(self):
        return self.__page_count

    @page_count.setter
    def page_count(self, value):
        self.__page_count = value

    def __str__(self):
        ret = super().__str__()
        return ret + f'Пробег: {self.page_count} стр. \n'


class Scanner(Equipment):
    def __init__(self, serial_number):
        super().__init__(serial_number, 's')
        self.__id = uuid4()
        self.__dpi = 400

    @property
    def dpi(self):
        return self.__dpi

    @dpi.setter
    def dpi(self, value):
        dpis = [400, 600, 800, 1200]
        if value in dpis:
            self.__dpi = value
        else:
            self.__dpi = 400

    def __str__(self):
        ret = super().__str__()
        return ret + f'Разрешение сканирования: {self.dpi} dpi. \n'


class Copier(Equipment):
    def __init__(self, serial_number):
        super().__init__(serial_number, 'c')
        self.__id = uuid4()


# Создадим два склада.
wh_main = WareHouse('Главный склад', 'Склад')
wh_main.postal_code = 400117
wh_main.postal_address = 'Волгоград, Тимирязева ул. 21 д.'
wh_add = WareHouse('Промежуточный склад', 'Склад')
wh_add.postal_code = 400117
wh_add.postal_address = 'Волгоград, Латошинская ул. 104 д. А литер.'
wh_add.kpp = 342010201
# Создадим принтер
my_printer = Printer('E4544F1KNPRINT')
my_printer.price = 19900
my_printer.page_count = 45332
# Создадим сканер.
my_scanner = Scanner('E4544F1KZSCAN')
my_scanner.price = 16450
my_scanner.dpi = 800
# Покажем информацию о наших элементах.
print(wh_main)
print(wh_add)
print(my_printer)
print(my_scanner)

# Тестируем приходы и списания.
wh_main.add_in_stock(my_printer)
print(wh_main)
wh_main.del_from_stock(my_scanner)
wh_main.del_from_stock(my_printer)
wh_main.del_from_stock(my_printer)
# Проверим как можно перечислить остатки на складе.
# Оприходуем на запасной склад - пару единиц.
wh_add.add_in_stock(my_printer)
wh_add.add_in_stock(my_scanner)
# Ну и покажем их.
for el in wh_add:
    print('Элемент склада: ', el)
