'''
Реализовать класс Stationery (канцелярская принадлежность):
определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
в каждом классе реализовать переопределение метода draw. Для каждого класса метод должен выводить уникальное сообщение;
создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

'''


class Stationery():
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f'Метод рисует с помощью инструмента: {self.title} (Это класс {self.__class__.__name__})')


class Pen(Stationery):
    def __init__(self):
        super().__init__('Ручка')

    def draw(self):
        print(f'Метод рисует с помощью инструмента: {self.title} (Это класс {self.__class__.__name__})')


class Pencil(Stationery):
    def __init__(self):
        super().__init__('Карандаш')

    def draw(self):
        print(f'Метод рисует с помощью инструмента: {self.title} (Это класс {self.__class__.__name__})')


class Handle(Stationery):
    def __init__(self):
        super().__init__('Маркер')

    def draw(self):
        print(f'Метод рисует с помощью инструмента: {self.title} (Это класс {self.__class__.__name__})')


# Тесты
my_pen = Pen()
my_pen.draw()

my_pencil = Pencil()
my_pencil.draw()

my_handle = Handle()
my_handle.draw()
