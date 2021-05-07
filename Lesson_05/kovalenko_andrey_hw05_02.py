'''
*(вместо 1) Решить задачу генерации нечётных чисел от 1 до n (включительно), не используя ключевое слово yield.
'''


def odd_nums(max_numbers=15):
    # Наш генератор.
    return (el for el in range(1, max_numbers + 1, 2))


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
