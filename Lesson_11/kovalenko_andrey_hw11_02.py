'''
Создать собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
Проверить его работу на данных, вводимых пользователем.
При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
'''


# тут мы перехватывем сообщение об ошибке
class DivisionByZero(Exception):
    def __init__(self, message="Ошибка, деление на ноль!"):
        self.message = message
        super().__init__(self.message)


# Простенькая функция, которая делит одно на другое.
def divider(fd=0, sd=0):
    try:
        return fd / sd
    except ZeroDivisionError:
        return DivisionByZero('Ошибка деления на ноль.')


# test
print(divider(10, 2))
print(divider(11, 4))
print(divider(7, 0))
print(divider(10, 5))
print(divider(1, 455))
