'''
Написать декоратор для логирования типов позиционных аргументов функции, например:
def type_logger...
    ...
@type_logger
def calc_cube(x):
   return x ** 3

a = calc_cube(5)
5: <class 'int'>

Примечание: если аргументов несколько - выводить данные о каждом через запятую;
можете ли вы вывести тип значения функции?
Сможете ли решить задачу для именованных аргументов?

Сможете ли вы замаскировать работу декоратора?
Сможете ли вывести имя функции, например, в виде:

a = calc_cube(5)
calc_cube(5: <class 'int'>)
'''


def ex_decorator(func):
    def wrapper(*args, **kwargs):
        # Для неименованных аргументов
        for i in args:
            print(f'{str(func).split()[1]}({i}: {type(i)})')
        for i in kwargs:
            # Для именованных аргументов.
            print(f'{str(func).split()[1]}([ARG: {i}] = {kwargs[i]}: {type(kwargs[i])})')
        # Надо отдать обертке возврат декорируемой функции.
        return func(*args, **kwargs)

    # И вернуть обертку.
    return wrapper


# Декоратор
@ex_decorator
def function_with_arguments(a, b, c, d):
    try:
        b = int(b)
        b = b ** 3
    except:
        b = 0
    return b


# Передаем что угодно, КАК угодно.
print(f'Результат функции, обернутой декоратором: {function_with_arguments(a="TEXT", b=2, c=555, d={1: "2"})}')
