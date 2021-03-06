'''
Дан список:
['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
Необходимо его обработать — обособить каждое целое число (вещественные не трогаем) кавычками
(добавить кавычку до и кавычку после элемента списка, являющегося числом) и дополнить нулём до двух целочисленных разрядов:
['в', '"', '05', '"', 'часов', '"', '17', '"', 'минут', 'температура', 'воздуха', 'была', '"', '+05', '"', 'градусов']
Сформировать из обработанного списка строку: в "05" часов "17" минут температура воздуха была "+05" градусов
Подумать, какое условие записать, чтобы выявить числа среди элементов списка? Как модифицировать это условие для чисел со знаком?
Примечание: если обособление чисел кавычками не будет получаться - можете вернуться к его реализации позже.
Главное: дополнить числа до двух разрядов нулём!
*Решить задачу 2 не создавая новый список (как говорят, in place). Эта задача намного серьёзнее,
чем может сначала показаться. (задача проще :))

'''

# У нас чуть больший список, проверяем универсальность алгоритма.
# some_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
some_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов', 'то', 'есть', 'выше',
             '-1', 'градуса']
some_list_as_text = ''
# Тут нам запретили создавать новый список, не будем делать этого вообще.
# Вместо этого обернем логикой инкрементируемое значение в циле while.
idx = 0

while idx < len(some_list):
    el = some_list[idx]
    if el.replace('+', '').replace('-', '').isdigit():
        some_list.insert(idx, '"')
        some_list[idx + 1] = some_list[idx + 1].replace(el, "%0.2d" % int(el))
        some_list_as_text = some_list_as_text + ' "' + some_list[idx + 1] + '"'
        some_list.insert(idx + 2, '"')
        id += 3
    else:
        id += 1
        some_list_as_text = some_list_as_text + ' ' + el

print(some_list_as_text)
