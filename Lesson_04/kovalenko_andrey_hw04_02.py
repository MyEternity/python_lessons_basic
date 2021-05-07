'''
Написать функцию currency_rates(), принимающую в качестве аргумента код валюты (например, USD, EUR, GBP, ...)
и возвращающую курс этой валюты по отношению к рублю.

Использовать библиотеку requests.
В качестве API можно использовать http://www.cbr.ru/scripts/XML_daily.asp.
Рекомендация: выполнить предварительно запрос к API в обычном браузере, посмотреть содержимое ответа.
Можно ли, используя только методы класса str, решить поставленную задачу?
Функция должна возвращать результат числового типа, например float.
Подумайте: есть ли смысл для работы с денежными величинами использовать вместо float тип Decimal?
Сильно ли усложняется код функции при этом?
Если в качестве аргумента передали код валюты, которого нет в ответе, вернуть None.
Можно ли сделать работу функции не зависящей от того, в каком регистре был передан аргумент?
В качестве примера выведите курсы доллара и евро.
'''

# По ТЗ
import requests

# Если нужно использовать типа данных Decimal
# Здесь будем хранить данные с сайта.
reply_dict = {}


def xml_reply_replaces(input_line=""):
    # Делаем серию замен.
    processing_text = input_line.replace("<ValCurs Date=", "")
    processing_text = processing_text.replace('<?xml version="1.0" encoding="windows-1251"?>', "")
    processing_text = processing_text.replace('" name="Foreign Currency Market">', "")
    processing_text = processing_text.replace("<Valute ID=", "#")
    processing_text = processing_text.replace("</Valute>", "")
    processing_text = processing_text.replace("><NumCode>", "--")
    processing_text = processing_text.replace("</NumCode><CharCode>", "--")
    processing_text = processing_text.replace("</CharCode><Nominal>", "--")
    processing_text = processing_text.replace("</Nominal><Name>", "--")
    processing_text = processing_text.replace("</Name><Value>", "--")
    processing_text = processing_text.replace("</Value>", "")
    processing_text = processing_text.replace("</ValCurs>", "")
    processing_text = processing_text.replace('"', "")
    # Проходим по данным
    for current_pair in processing_text.split("#"):
        # Каждая пара у нас в результате замен - оказалась разделена --
        line = current_pair.split("--")
        if len(line) > 1:
            # Заполняем словарь данными по найденным парам.
            if line[2].lower() not in reply_dict.keys():
                dcm = float(line[5].replace(",", ".")) / float(line[3].replace(",", "."))
                # Decimal или Float? Лучше FLOAT)
                # reply_dict[line[2].lower()] = Decimal(dcm)
                reply_dict[line[2].lower()] = dcm
    return reply_dict


def currency_rates(currency="USD"):
    # Получим данные с сайта.
    response = xml_reply_replaces(requests.get("http://www.cbr.ru/scripts/XML_daily.asp", "").text)
    # Заполним словарь для ответа.
    reply = {currency: response.get(currency.lower(), "None")}
    return reply


# Заполним массив, чтобы не дублировать код вывода.
currency_array = ['uSd', 'eur', "AuD"]  # Валютные индексы - не регистрозависимы.
for el in currency_array:
    # Возвращается словать с timestamp, и парой.
    data_info = currency_rates(el)
    # Покажем информацию.
    print(f'Валюта {el.upper()}, курс = {data_info.get(el)}')
