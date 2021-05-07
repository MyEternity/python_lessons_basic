'''
Реализуйте базовый класс Car:
у класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);

опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;

добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат. Вызовите методы и покажите результат.

'''


class Car():
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'Машина "{self.color} {self.name}" поехала.'

    def stop(self):
        return f'Машина "{self.color} {self.name}" остановилась'

    def turn(self, direction):
        directions = {"r": "направо", "l": "налево"}
        if direction in directions.keys():
            return f'Машина "{self.color} {self.name}" повернула {directions[direction]}'
        else:
            return f'Машина "{self.color} {self.name}" не может выполнить поворот. Недопустимое направление (r/l)?'

    def show_speed(self):
        return f'Скорость машины "{self.color} {self.name}" {self.speed} км/ч'


class TownCar(Car):
    def show_speed(self):
        if self.speed <= 60:
            return f'Скорость машины "{self.color} {self.name}" {self.speed} км/ч'
        else:
            return f'Превышение скорости!'


class SportCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def show_speed(self):
        if self.speed <= 40:
            return f'Скорость машины "{self.color} {self.name}" {self.speed} км/ч'
        else:
            return f'Превышение скорости!'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)
        self.is_police = True


c1 = TownCar(10, 'Белая', 'Камри')
print(c1.go())
c1.speed = 100
print(c1.turn('l'))
print(c1.show_speed())

c2 = PoliceCar(140, 'Синий', 'Ford')
c2.speed = 150
print(c2.show_speed())
