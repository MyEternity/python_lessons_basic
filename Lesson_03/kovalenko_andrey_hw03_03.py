'''
Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников и возвращающую словарь,
в котором ключи — первые буквы имён, а значения — списки, содержащие имена, начинающиеся с соответствующей буквы.
Например:
thesaurus("Иван", "Мария", "Петр", "Илья")
{
 "И": ["Иван", "Илья"],
 "М": ["Мария"], "П": ["Петр"]
}
Подумайте: полезен ли будет вам оператор распаковки?
Как поступить, если потребуется сортировка по ключам?
Можно ли использовать словарь в этом случае?
'''


def thesaurus(*args):
    # Объявим словарь
    names_dict = {}
    # Отбираем каждый элемент переданного массива.
    # Сортируем по ключикам
    for i in sorted(args):
        # Проверяем существует ли индекс
        if names_dict.keys() != i[0]:
            # Фильтруем те элементы, которые подходят + сортируем их
            names_dict[i[0]] = list(sorted(filter(lambda x: str(x[0]).lower() == str(i[0]).lower(), args)))
    return names_dict


print(thesaurus("Иван", "Мария", "Петр", "Илья", "Иннокентий", "Владимир", "Дмитрий"))
