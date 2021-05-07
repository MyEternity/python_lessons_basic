'''
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц: 3 на 2, 3 на 3, 2 на 4.

31 22
37 43
51 86

3 5 32
2 4 6
-1 64 -8

3 5 8 3
8 3 7 1

Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для  сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно.
Первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и пр
'''

from uuid import uuid4


class Matrix:
    __eol_sym__ = chr(13) + chr(10)

    def __init__(self, in_list_of_list):
        '''
            Класс, хранящий матрицу, создаваемую из списка списков.
            :param in_list_of_list: Список списков [[v1, v2], [v2, v4], [v5, v2]]
        '''
        # Проверим что прислали именно прямоугольный список списков.
        len_base = len(in_list_of_list[0])
        high_base = len(in_list_of_list)
        for x in in_list_of_list:
            if len_base != len(x):
                raise Exception('Некорректная матрица')
        self.identity = uuid4()  # Каждая матрица имееет свой уникальный гуид.
        self.height = high_base  # Высота
        self.width = len_base  # Ширина
        self.in_list_of_list = in_list_of_list  # Тут храним саму матрицу.

    def __str__(self):
        '''
            Метод перекрывает строковый вывод класса.
            :return: Вернет строковое представление матрицы.
        '''
        ret_line = f'Матрица ID: {self.identity}' + self.__eol_sym__ + \
                   f'Размер: {self.width} x {self.height}' + self.__eol_sym__

        for x in self.in_list_of_list:
            for y in x:
                ret_line = ret_line + str(y) + ' '
            ret_line = ret_line + self.__eol_sym__
        return ret_line

    def __add__(self, other):
        '''
            Сложение матриц.
            :param other: Матрица, которую нужно прибавить. Для успешного сложения требуется строгое соотв. размерности.
            :return: Новая матрица, каждый элемент которой = сумме элементов складываемых матриц.
        '''
        result_list = []
        if self.width == other.width and self.height == other.height:
            for i in range(len(self.in_list_of_list)):
                result_line = []
                for j in range(len(self.in_list_of_list[i])):
                    result_line.append(self.in_list_of_list[i][j] + other.in_list_of_list[i][j])
                result_list.append(result_line)
            return Matrix(result_list)
        else:
            raise Exception('Матрицы отличаются размерами, сложение невозможно!')


# Unit test
mx1 = Matrix([[1, 2, 3], [3, 4, 5], [5, 5, 5], [8, 2, 1]])
print(mx1)

mx2 = Matrix([[1, 1, 1], [1, 1, 1], [1, 1, 1], [10, 10, 10]])
print(mx2)

mx3 = mx1 + mx2
print(mx3)
