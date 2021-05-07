'''
Написать декоратор с аргументом-функцией (callback),
позволяющий валидировать входные значения функции и выбрасывать исключение ValueError, если что-то не так, например:
def val_checker...
    ...
@val_checker(lambda x: x > 0)
def calc_cube(x):
   return x ** 3

a = calc_cube(5)
125
a = calc_cube(-5)
Traceback (most recent call last):
  ...
    raise ValueError(msg)
ValueError: wrong val -5
Примечание: сможете ли вы замаскировать работу декоратора?
'''


def ex_decorator(f):
    def _ex_decorator(func):
        def wrapper(*args):
            l1 = set(args)
            l2 = set(filter(f, args))
            for i in l2:
                for i in l1 - l2:
                    raise ValueError(f'wrong val {i}')
                return func(i)

        return wrapper

    return _ex_decorator


# Декоратор
@ex_decorator(lambda x: x > 0)
def calc_cube(b):
    return b ** 3


# Строку мы не жуем.
print(calc_cube(4))
