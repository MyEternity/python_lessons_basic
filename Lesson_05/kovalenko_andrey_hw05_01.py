'''
Написать генератор нечётных чисел от 1 до n (включительно), используя ключевое слово yield, например:
odd_to_15 = odd_nums(15)
next(odd_to_15)
1
next(odd_to_15)
3
...
next(odd_to_15)
15
next(odd_to_15)
...StopIteration...
'''


# Наша функция, которая работает как генератор.
def odd_nums(max_number=15):
    for i in range(1, max_number + 1, 2):
        yield i


# Тестируем.
odd_number_15 = odd_nums(15)
print(next(odd_number_15))
print(next(odd_number_15))
print(next(odd_number_15))
print(next(odd_number_15))
print(next(odd_number_15))
print(next(odd_number_15))
print(next(odd_number_15))
print(next(odd_number_15))
# Тут Генератор будет истощен.
print(next(odd_number_15))
