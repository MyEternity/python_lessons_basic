'''
Реализовать проект «Операции с комплексными числами».
Создать класс «Комплексное число».
Реализовать перегрузку методов сложения и умножения комплексных чисел.
Проверить работу проекта.
Для этого создать экземпляры класса (комплексные числа), выполнить сложение и умножение созданных экземпляров.
Проверить корректность полученного результата.
'''


class ComplexNumber:
    def __init__(self, real_value, imaginary_value):
        self.__real_value = real_value
        self.__imaginary_value = imaginary_value

    @property
    def rv(self):
        return self.__real_value

    @property
    def iv(self):
        return self.__imaginary_value

    @property
    def number(self):
        if self.iv < 0:
            if self.iv != -1:
                return f'{self.rv}{self.iv}i'
            else:
                return f'{self.rv}-i'
        else:
            if self.iv == 1:
                return f'{self.rv}+i'
            else:
                return f'{self.rv}+{self.iv}i'

    def __str__(self):
        return self.number

    def __add__(self, other):
        if type(other) == ComplexNumber:
            new_rv = self.rv + other.rv
            new_iv = self.iv + other.iv
            return ComplexNumber(new_rv, new_iv)
        else:
            print('Комплексное число можно складывать только с другим комплексным числом!')
            return 0

    def __mul__(self, other):
        if type(other) == ComplexNumber:
            # Перемножение мнимых частей - дает действительное чило * -1, учтем это.
            new_rv = self.rv * other.rv + self.iv * other.iv * -1
            # Переможножение любой мнимой и действительной части - дает мнимую часть.
            new_iv = self.rv * other.iv + self.iv * other.rv
            return ComplexNumber(new_rv, new_iv)
        else:
            print('Комплексное число можно перемножать только с другим комплексным числом!')
            return 0


n1 = ComplexNumber(3, 1)
n2 = ComplexNumber(2, -3)
n3 = ComplexNumber(1, -1)
# вывод числа (можно также пользоваться свойством number
print(n3)
# Сложение.
print(n1 + n2)
# Умножение
print(n1 * n2)
