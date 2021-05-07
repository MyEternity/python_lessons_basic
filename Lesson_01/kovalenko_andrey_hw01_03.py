'''
Реализовать склонение слова «процент» для чисел до 20.
Например, задаем число 5 — получаем «5 процентов»,
задаем число 2 — получаем «2 процента». Вывести все склонения для проверки.
'''

# Заполним массив склоннеий.
percent_syn = []
percent_max = 121  # Можно задать любое число (по условиям задачи - 20)

# Нужно смотреть остаток от деления на 10
while percent_max >= 0:
    # Есть исключения - в каждой сотне значения с 11 по 20 имеют склонение-исключение.
    # Получать два последних символа из строки можно только от длины 2+
    if percent_max > 10:
        if 10 < int(str(percent_max)[-2] + str(percent_max)[-1]) < 19:
            value = 0
        else:
            value = percent_max % 10
    else:
        value = percent_max % 10

    # Склонения
    if value in [0, 5, 6, 7, 8, 9]:
        percent_syn.append([percent_max, 'процентов'])
    elif value in [2, 3, 4]:
        percent_syn.append([percent_max, 'процента'])
    else:
        percent_syn.append([percent_max, 'процент'])
    percent_max -= 1

# Выведем наш массив в обратном порядке.
for t in range(len(percent_syn) - 1, -1, -1):
    print(percent_syn[t][0], percent_syn[t][1])
