'''
Доработать предыдущую функцию в num_translate_adv():
реализовать корректную работу с числительными, начинающимися с заглавной буквы —
результат тоже должен быть с заглавной. Например: num_translate_adv("One") - "Один"
num_translate_adv("two") - "два"

'''


def num_translate_adv(in_number):
    # Храним данные в словаре.
    data = {
        'one': 'один',
        'two': 'два',
        'three': 'три',
        'four': 'четыре',
        'five': 'пять',
        'six': 'шесть',
        'seven': 'семь',
        'eight': 'восемь',
        'nine': 'девять',
        'ten': 'десять'
    }
    # Проверим регистр первого символа.
    if in_number[0].islower():
        # вернем данные в нижнем регистре.
        return data.get(in_number.lower(), 'None').lower()
    else:
        # вернем данные методом capitalize
        return data.get(in_number.lower(), 'None').capitalize()


print(num_translate_adv('Twenty'))
