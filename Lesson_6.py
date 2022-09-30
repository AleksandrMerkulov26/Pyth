# 1. Создать класс TrafficLight (светофор).
# определить у него один атрибут color (цвет) и метод running (запуск);
# атрибут реализовать как приватный;
# в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
# продолжительность первого состояния (красный) составляет 7 секунд, второго (жёлтый) — 2 секунды, третьего (зелёный) — на ваше усмотрение;
# переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
# проверить работу примера, создав экземпляр и вызвав описанный метод.
# import time
#
# class TrafficLight:
#
#     __traffic_light_color = "Светофор"
#
#     def running(self):
#         while True:
#             print("Red light")
#             time.sleep(7)
#             print("Yellow light")
#             time.sleep(2)
#             print("Green light")
#             time.sleep(7)
#
#
# a = TrafficLight()
# a.running()
# print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')

# 2. Реализовать класс Road (дорога).
# определить атрибуты: length (длина), width (ширина);
# значения атрибутов должны передаваться при создании экземпляра класса;
# атрибуты сделать защищёнными;
# определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
# использовать формулу: длина*ширина*масса асфальта для покрытия одного кв. метра дороги асфальтом, толщиной в 1 см*число см толщины полотна;
# проверить работу метода.
# # class Road:
#
#     def __init__(self, length, width):
#         self._length = length
#         self._width = width
#         self.weight = 25
#         self.height = 5
#
#     def asphalt_mass(self):
#         asphalt_mass = self._length * self._width * self.weight * self.height / 1000
#         print(f'Для покрытия всего дорожного полотна неободимо {round(asphalt_mass)} тонн асфальта')
#
#
# try:
#     my_length = int(input('Введите длинну дорожного полотна, м: '))
#     my_width = int(input('Введите ширину дорожного полотна, м: '))
#     r = Road(my_length, my_width)
#     r.asphalt_mass()
# except ValueError:
#     print('Требуется ввести число, а не строку символов')
# print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')

# 3. Реализовать базовый класс Worker (работник).
# определить атрибуты: name, surname, position (должность), income (доход);
# последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus};
# создать класс Position (должность) на базе класса Worker;
# в классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учётом премии (get_total_income);
# проверить работу примера на реальных данных: создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров.

# class Worker:
#
#     def __init__(self, name, surname, position, wage, bonus):
#         self.name = name
#         self.surname = surname
#         self.position = position
#         self._income = {"wage": int(wage), "bonus": int(bonus)}
#
#
# class Position(Worker):
#     def __init__(self, name, surname, position, wage, bonus):
#         super().__init__(name, surname, position, wage, bonus)
#
#     def get_full_name(self):
#         return 'Имя и фамилия сотрудника: ' + self.name + ' ' + self.surname + '\n'
#
#     def get_total_income(self):
#         return 'Доход с учетом премии: ' + str(self._income["wage"] + self._income["bonus"]) + ' р.'
#
#
# try:
#     new_name = input('Введите имя сотрудника: ')
#     new_surname = input('Введите фамилию сотрудника: ')
#     new_position = input('Введите должность сотрудника: ')
#     new_wage = int(input('Введите оклад сотрудника, р.: '))
#     new_bonus = int(input('Введите премию сотрудника, р.: '))
#
#     p = Position(new_name, new_surname, new_position, new_wage, new_bonus)
#     print(p.get_full_name(), p.get_total_income())
# except ValueError:
#     print('Требуется ввести число, а не строку символов')

# 4. Реализуйте базовый класс Car.
# у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# class Car:
#     def __init__(self, speed, color, name, is_police=False):
#         self.speed = speed
#         self.color = color
#         self.name = name
#         self.is_police = is_police
#
#     def go(self):
#         return f'Автомобиль {self.name} поехал.'
#
#     def stop(self):
#         return f'\nАвтомобиль {self.name} остановился.'
#
#     def turn(self, direction):
#         return f'\nАвтомобиль {self.name} повернул {direction}'
#
#     def show_speed(self):
#         return f'\nТекущая скорость автомобиля равна: {self.speed}'
#
#
# class TownCar(Car):
#     def show_speed(self):
#         if self.speed > 60:
#             return f'\nВаша скорость превышает допустимую! Скрость равна: {self.speed}'
#         else:
#             return f'\nСейчас ваша скорость равна: {self.speed}. И она допустима.'
#
#
# class SportCar(Car):
#     pass
#
#
# class WorkCar(Car):
#     def show_speed(self):
#         if self.speed > 40:
#             return f'\nВаша скорость превышает допустимую! Скрость равна: {self.speed}'
#         else:
#             return f'\nСейчас ваша скорость равна: {self.speed}. И она допустима.'
#
#
# class PoliceCar(Car):
#     pass
#
#
# town = TownCar(70, 'blue', 'Киа', False)
# print('1:\n' + town.go(), town.show_speed(), town.turn('left'), town.stop())
#
# sport = SportCar(170, 'red', 'Феррари', False)
# print('2:\n' + sport.go(), sport.show_speed(), sport.turn('left'), sport.stop())
#
# work = WorkCar(30, 'red', 'Камаз', False)
# print('3:\n' + work.go(), work.show_speed(), work.turn('right'), work.stop())
#
# police = PoliceCar(100, 'yellow', 'Форд', True)
# print('4:\n' + police.go(), police.show_speed(), police.turn('right'), police.stop())
# print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')

# 5. Реализовать класс Stationery (канцелярская принадлежность).
# определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
# создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
# в каждом классе реализовать переопределение метода draw. Для каждого класса метод должен выводить уникальное сообщение;
# создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
# class Stationery:
#     def __init__(self, title):
#         self.title = title
#
#     def draw(self):
#         return f'Запуск отрисовки'
#
#
# class Pen(Stationery):
#     def draw(self):
#         return f'Сейчас запущена отрисовка {self.title}'
#
#
# class Pencil(Stationery):
#     def draw(self):
#         return f'Сейчас запущена отрисовка {self.title}'
#
#
# class Handle(Stationery):
#     def draw(self):
#         return f'Сейчас запущена отрисовка {self.title}'
#
#
# my_pen = Pen('ручкой')
# print(my_pen.draw())
# my_pencil = Pencil('карандашем')
# print(my_pencil.draw())
# my_handle = Handle('маркером')
# print(my_handle.draw())
# print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')