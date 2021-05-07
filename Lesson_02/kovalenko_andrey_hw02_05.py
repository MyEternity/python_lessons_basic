'''
Создать вручную список, содержащий цены на товары (10–20 товаров), например:
    [57.8, 46.51, 97, ...]
 Вывести на экран эти цены через запятую в одну строку, цена должна отображаться в виде <r> руб <kk> коп
(например «5 руб 04 коп»).
 Подумать, как из цены получить рубли и копейки, как добавить нули, если, например,
получилось 7 копеек или 0 копеек (должно быть 07 коп или 00 коп).
 Вывести цены, отсортированные по возрастанию, новый список не создавать
(доказать, что объект списка после сортировки остался тот же).
 Создать новый список, содержащий те же цены, но отсортированные по убыванию.
 Вывести цены пяти самых дорогих товаров. Сможете ли вывести цены этих товаров по возрастанию, написав минимум кода?

'''

# Создаем список и заполняем его случайными числами. Пункт 1
import random

result_string = ''
awesome_result_string = ''

number_list = []

for i in range(0, 20, 1):
    value = (round(random.random() * 100, 2));
    # Великий бог рандома редко выдает 00 копеек, поэтому заставим наш массив заполняться нулевыми копейками
    # в определенных случаях)
    if 30 < value < 50:
        value = value // 1
    number_list.append(value)
    element = number_list[len(number_list) - 1]
    # print(f'{element // 1:02.00f} {int(element % 1 * 100): 02d}')
    # Остатки от деления и целочисленный результат - работают не точно!
    # Собираем цены без лидирующих нулей пункт 2
    result_string = result_string + f'{int(str(element).split(".")[0])} руб. {int(str(element).split(".")[1]):02d} коп., '
    # Выводим красивые цены) пункт 3.
    awesome_result_string = awesome_result_string + f'{int(str(element).split(".")[0]):02d} руб. {int(str(element).split(".")[1]):02d} коп., '

print(f'Рубли без лидирующих нулей: {result_string}')
print(f'Список с лидирующими нулями ({id(number_list)}): {awesome_result_string}')

# Отсортируем список.
awesome_result_string = ''
number_list.sort()

for i in number_list:
    awesome_result_string = awesome_result_string + f'{int(str(i).split(".")[0]):02d} руб. {int(str(i).split(".")[1]):02d} коп., '

# Выведем.
print(f'Отсортированный список ({id(number_list)}):  {awesome_result_string}')

reverse_number_list = list(reversed(number_list))
# Сортируем в обратном порядке. №4
print(f'Сортировка по убыванию ({id(reverse_number_list)}): {reverse_number_list}')
# Минмум кода для вывода самых высоких (5 шт) цен - №5 по возрастанию
print(reverse_number_list[4::-1])
