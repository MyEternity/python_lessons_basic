'''
*(вместо 2) Доработать функцию currency_rates(): теперь она должна возвращать кроме курса дату,
которая передаётся в ответе сервера.
Дата должна быть в виде объекта date.

Подумайте, как извлечь дату из ответа, какой тип данных лучше использовать в ответе функции?
'''

# Импортируем модуль для работы с датй-временем.
import datetime as dt

# По ТЗ
import requests

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
    # Определяем дату получения информации о курсах.
    dict_date = dt.datetime.strptime(processing_text.split("#")[0], "%d.%m.%Y").date()
    # Будем хранить ее в ключе "timestamp"
    reply_dict["timestamp"] = dict_date
    reply_dict["last_update_dts"] = dt.datetime.now()
    # Проходим по данным
    for current_pair in processing_text.split("#"):
        # Каждая пара у нас в результате замен - оказалась разделена --
        line = current_pair.split("--")
        if len(line) > 1:
            # Заполняем словарь данными по найденным парам.
            if line[2].lower() not in reply_dict.keys():
                reply_dict[line[2].lower()] = float(line[5].replace(",", ".")) / float(line[3].replace(",", "."))
    return reply_dict


def currency_rates(currency="USD"):
    # Перечитаем данные с сайта только если еще не получали их.
    if reply_dict.get('last_update_dts', 0) == 0:
        response = xml_reply_replaces(requests.get("http://www.cbr.ru/scripts/XML_daily.asp", "").text)
    else:
        response = reply_dict
    # Заполним словарь для ответа.
    reply = {'timestamp': response.get("timestamp", "None"), currency: response.get(currency.lower(), "None")}
    return reply


# Заполним массив, чтобы не дублировать код вывода.
currency_array = ['uSd', 'eur', "AuD"]  # Валютные индексы - не регистрозависимы.
for el in currency_array:
    # Возвращается словать с timestamp, и парой.
    data_info = currency_rates(el)
    # Покажем информацию.
    print(f'Валюта {el.upper()}, курс = {data_info.get(el)} на дату: {data_info.get("timestamp")}')
