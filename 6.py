# 1. Создать класс TrafficLight (светофор).
# определить у него один атрибут color (цвет) и метод running (запуск);
# атрибут реализовать как приватный;
# в рамках метода реализовать переключение светофора в режимы: красный,
# жёлтый, зелёный;
# продолжительность первого состояния (красный) составляет 7 секунд, 
# второго (жёлтый) — 2 секунды, третьего (зелёный) — на ваше усмотрение;
# переключение между режимами должно осуществляться только в указанном
# порядке (красный, жёлтый, зелёный);
# проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов. При его
# нарушении выводить соответствующее сообщение и завершать скрипт.

import time

class TraffictLight:
    __color = ('red', 'yellow', 'green')

    def running(self):
        while True:
            if "".join(self.__color) == 'redyellowgreen':
                for i in range(3):
                    print(self.__color[0])
                    time.sleep(7)
                    print(self.__color[1])
                    time.sleep(2)
                    print(self.__color[2])
                    time.sleep(4)
                return "Stop for service"
            else:
                return "Wrong order"

lighter = TraffictLight()
lighter.running()

# 2. Реализовать класс Road (дорога).
# определить атрибуты: length (длина), width (ширина);
# значения атрибутов должны передаваться при создании экземпляра 
# класса;
# атрибуты сделать защищёнными;
# определить метод расчёта массы асфальта, необходимого для покрытия
# всей дороги;
# использовать формулу: длина*ширина*масса асфальта для покрытия 
# одного кв. метра дороги асфальтом, толщиной в 1 см*число см толщины
# полотна;
# проверить работу метода.
# Например: 20 м*5000 м*25 кг*5 см = 12500 т.

class Road:
    def __init__(self, l=20, w=5000):
        self._length = l
        self._width = w

    def asphalt_mass(self):
        return (self._length * self._width * 125 / 1000)

asp = Road(1, 2000)
print(f"Для покрытия нужно {round(asp.asphalt_mass())} т. асфальта")

# 3. Реализовать базовый класс Worker (работник).
# определить атрибуты: name, surname, position (должность), income 
# (доход);
# последний атрибут должен быть защищённым и ссылаться на словарь, 
# содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus};
# создать класс Position (должность) на базе класса Worker;
# в классе Position реализовать методы получения полного имени сотрудника
# (get_full_name) и дохода с учётом премии (get_total_income);
# проверить работу примера на реальных данных: создать экземпляры класса
# Position, передать данные, проверить значения атрибутов, вызвать 
# методы экземпляров.

class Worker:
    def __init__(self, n=None, s=None, p=None, i=None):
        self.name = n
        self.surname = s
        self.position = p
        self._income = i

class Position(Worker):
    def __init__(self, name, surname, position, _income):
        super().__init__(name, surname, position, _income)

    def get_full_name(self):
        return self.name + " " + self.surname

    def get_total_income(self):
        return sum(self._income.values())

income = {"wage": 10000, "bonus": 253}
workers = Position('Ivan', 'Ivanov', 'worker', income)
print(workers.get_full_name(), workers.get_total_income())


# 4. Реализуйте базовый класс Car.
# у класса должны быть следующие атрибуты: speed, color, name, is_police
# (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, 
# что машина поехала, остановилась, повернула (куда);
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать
# текущую скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed. При
# значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться
# сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните
# доступ к атрибутам, выведите результат. Вызовите методы и покажите
# результат.

class Car:
    def __init__(self, color, name, speed, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print("Машина едет")
        self.speed += 5

    def stop(self):
        print("Машина остановилась")
        self.speed = 0

    def turn(self, direction):
        print("Машина повернула на{0}".format(direction))

    def show_speed(self):
        return self.speed

class TownCar(Car):
    def __init__(self, color, name, speed=0, is_police=False):
        super().__init__(color, name, speed, is_police)

    def show_speed(self):
        print(self.speed)
        if self.speed > 60:
            print("Превышение скорости")

class SportCar(Car):
    def __init__(self, color, name, speed=0, is_police=False):
        super().__init__(color, name, speed, is_police)

class WorkCar(Car):
    def __init__(self, color, name, speed=0, is_police=False):
        super().__init__(color, name, speed, is_police)

    def show_speed(self):
        print(self.speed)
        if self.speed > 40:
            print("Превышение скорости")

class PoliceCar(Car):
    def __init__(self, color, name, speed=0, is_police=True):
        super().__init__(color, name, speed, is_police)

def car_test(car):
    print(car.color, car.name, car.speed, car.is_police)
    for i in range(13):
        car.go()
        car.show_speed()
    car.turn("право")
    car.turn("лево")
    car.stop()

cars = [TownCar("green", "VW"),
        WorkCar("yellow", "Ford"),
        SportCar("red", "OOOO"),
        PoliceCar("white", "Ford")]

for i in cars:
    car_test(i)

# 5. Реализовать класс Stationery (канцелярская принадлежность).
# определить в нём атрибут title (название) и метод draw (отрисовка). 
# Метод выводит сообщение «Запуск отрисовки»;
# создать три дочерних класса Pen (ручка), Pencil (карандаш), 
# Handle (маркер);
# в каждом классе реализовать переопределение метода draw. Для каждого 
# класса метод должен выводить уникальное сообщение;
# создать экземпляры классов и проверить, что выведет описанный метод 
# для каждого экземпляра.

class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки")

class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print("Запуск отрисовки ручкой")

class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print("Запуск отрисовки карандашом")

class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print("Запуск отрисовки маркером")

for i in [Stationery("Parker"), Pen("pen"), Pencil("pencil"), Handle("pencil")]:
    i.draw()
