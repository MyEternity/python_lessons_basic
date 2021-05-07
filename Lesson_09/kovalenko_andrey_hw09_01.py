'''
Создать класс TrafficLight (светофор): определить у него один атрибут color (цвет) и метод running (запуск);
атрибут реализовать как приватный;

в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;

продолжительность первого состояния (красный) составляет 7 секунд, второго (жёлтый) — 2 секунды, третьего (зелёный)
    — на ваше усмотрение;

переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);

проверить работу примера, создав экземпляр и вызвав описанный метод.

Задачу можно усложнить, реализовав проверку порядка режимов. При его нарушении выводить соответствующее сообщение и
завершать скрипт.

'''
import time


def decor(func):
    def wrapper(*args):
        start_time = time.time()
        func(*args)
        end_time = time.time()
        print(f'Ожидание составило: {end_time - start_time} сек.')

    return wrapper


class TrafficLight:
    __color = 'red'
    # Проверку работы сфетофора построим на словаре.
    # Ключ - цвет.
    # Кортеж -
    # 0 - Задержка
    # 1 - Допустимый новый цвет.
    # 2 - Русификация (для красоты).
    __cl_data = {'red': (7, 'yellow', 'Красный'), 'yellow': (), 'green': (4, 'yellow', 'Зеленый')}
    # При прямой отработке - от красного к зеленому у желтого допустимый следующий цвет - зеленый.
    __direct_el = (2, 'green', 'Желтый')
    # При обратной - красный.
    __reverse_el = (2, 'red', 'Желтый')

    @decor
    # Для замеров времени переключения прилепим декоратор..
    def running(self, new_color):
        # Если цвет красный, то это прямая работа светофора.
        if self.__color == 'red':
            self.__cl_data['yellow'] = self.__direct_el
        # А если зеленый, то его надо реверсировать.
        elif self.__color == 'green':
            self.__cl_data['yellow'] = self.__reverse_el

        print(f'Сейчас светофор: {self.__cl_data[self.__color][2]}')
        if new_color == self.__cl_data[self.__color][1]:
            # Организуем задержку, и переключаем светофор
            ticker = self.__cl_data[self.__color][0]
            while ticker > 0:
                print(ticker)
                ticker = ticker - 1
                time.sleep(1)
            self.__color = new_color
            print(f'Цвет светофора сменился на: {self.__cl_data[self.__color][2]}')
        else:
            raise Exception('Некорректное значение нового цвета!')

    def current_l(self):
        return self.__cl_data[self.__color]

    # Следующее возможное значение цвета - выбирается автоматически.
    def next_color(self):
        self.running(self.__cl_data[self.__color][1])


# Тестируем наш светофор.
l1 = TrafficLight()
l1.running('yellow')
print(f'Текущий цвет: {l1.current_l()[2]}')
l1.next_color()  # Зеленый
l1.next_color()  # Желтый.
l1.next_color()  # Красный.
l1.next_color()  # Желтый.
l1.running('yellow')  # Провоцируем светофор на столкновение с машиной ГИБДД.
