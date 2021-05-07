'''
Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах:
a. до минуты: <s> сек;
b. до часа: <m> мин <s> сек;
c. до суток: <h> час <m> мин <s> сек;
d. * в остальных случаях: <d> дн <h> час <m> мин <s> сек.
'''

# В данном списке будем хранить набор для сборки окончательного сообщения.
message = []
# Продолжительность в секундах.
input_duration_seconds = input('Введите продолжительность времени в секундах: \n')
# на всякий случай, проверим что ввели челое число.
if input_duration_seconds.isdigit():
    duration_seconds = int(input_duration_seconds)
    # Посмотрим сколько у нас дней.
    duration_days = duration_seconds // (24 * 60 ** 2)
    duration_seconds = duration_seconds - duration_days * 24 * 60 ** 2
    message.append([duration_days, 'дн.'])
    # Проверим сколько у нас часов.
    duration_hours = duration_seconds // (60 ** 2)
    duration_seconds = duration_seconds - duration_hours * 60 ** 2
    message.append([duration_hours, 'час.'])
    # Посчитаем количество минут.
    duration_minutes = duration_seconds // 60
    duration_seconds = duration_seconds - duration_minutes * 60
    message.append([duration_minutes, 'мин.'])
    # Остались секунды.
    message.append([duration_seconds, 'сек.'])
    # Собираем сообщение:
    text_message = f'В промежутке времени: {input_duration_seconds} сек. содержится: '
    for i in message:
        # Собираем в строку только те элементы, которые не равны 0 и выводим их.
        if i[0] != 0:
            text_message = text_message + f'{str(i[0])} {i[1]} '
    print(text_message)
else:
    print('Интервал нужно вводить как целое число.')
