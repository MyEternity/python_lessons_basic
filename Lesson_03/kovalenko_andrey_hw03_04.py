'''
Написать функцию thesaurus_adv(), принимающую в качестве аргументов строки в формате «Имя Фамилия»
и возвращающую словарь, в котором ключи — первые буквы фамилий, а значения — словари,
реализованные по схеме предыдущего задания и содержащие записи, в которых фамилия начинается с соответствующей буквы.
Например:
thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")
{
 "А": {
   "П": ["Петр Алексеев"]
   },
 "С": {
  "И": ["Иван Сергеев", "Инна Серова"],
  "А": ["Анна Савельева"]
  }
}
Как поступить, если потребуется сортировка по ключам?
'''


def arr_data(*args):
    return list(args)


def thesaurus_adv(*args, key_sort=False):
    # Объявим словарь
    names_dict = {}
    if key_sort:
        # Не придумал ничего лучше, чем сортировать через отдельный список.
        sorted_list = list(args)
        sorted_list.sort(key=lambda x: str(x).split(' ')[1])
        args = sorted_list
    # Отбираем каждый элемент переданного массива.
    for i in args:
        for name, surname in arr_data(str(i).split()):
            # Проверяем существует ли индекс
            if surname[0] not in names_dict.keys():
                # Такого индекса нет, добавим для него словарь
                names_dict[surname[0]] = {}
                # И заполним данные словаря фильтром по всему массиву.
                if names_dict[surname[0]].keys() not in (surname[0], name[0]):
                    names_dict[surname[0]][name[0]] = []
                    names_dict[surname[0]][name[0]] = list(filter(lambda x:
                                                                  str(x).split()[0][0].lower() == str(
                                                                      name[0]).lower() and
                                                                  str(x).split()[1][0].lower() == str(
                                                                      surname[0]).lower(),
                                                                  args)
                                                           )
            else:
                # Такой индекс есть, нужно просто добавить для него новый список-массив
                names_dict[surname[0]][name[0]] = []
                names_dict[surname[0]][name[0]] = list(filter(lambda x:
                                                              str(x).split()[0][0].lower() == str(name[0]).lower() and
                                                              str(x).split()[1][0].lower() == str(surname[0]).lower(),
                                                              args)
                                                       )
    return names_dict


# Может потребоваться сортировка - передаем необязательный параметр key_sort
print(thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева", "Володька Путин",
                    "Димка Медведев", "Элла Чего-тоБулинна", key_sort=True))
