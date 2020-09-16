"""
4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. Выполните вызов
методов и также покажите результат.
"""


class Car:
    def __init__(self, speed: int, color: str, name: str, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    @staticmethod
    def go():
        print('The car went')

    @staticmethod
    def stop():
        print('The car stopped')

    @staticmethod
    def turn(direction: str):
        if direction == 'right':
            print('The car turned right')
        elif 'left' == direction:
            print('The car turned left')

    def show_speed(self):
        print(f'Current speed: {self.speed}')


class TownCar(Car):

    def show_speed(self):
        print(f'Current speed: {self.speed}')
        if self.speed > 60:
            print('Speed exceeded!')


class SportCar(Car):
    pass


class WorkCar(Car):

    def show_speed(self):
        print(f'Current speed: {self.speed}')
        if self.speed > 40:
            print('Speed exceeded!')


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
        self.is_police = True

town_car = TownCar(60, 'Black', 'Toyota Camry')
print(f'\nTownCar {town_car.name} {town_car.color}:')
town_car.go()
town_car.turn('left')
town_car.show_speed()
town_car.stop

sport_car = SportCar(110, 'Red', 'Ferrari')
print(f'\nSportCar {sport_car.name} {sport_car.color}:')
sport_car.go()
sport_car.show_speed()
sport_car.turn('right')

work_car = WorkCar(50, 'Green', 'Tractor')
print(f'\nWorkCar {work_car.name} {work_car.color}:')
work_car.go()
work_car.show_speed()

police_car = PoliceCar(60, 'Blue', 'Ford')
print(f'\nPoliceCar {police_car.name} {police_car.color}:')
police_car.go()
police_car.show_speed()
police_car.turn('left')
police_car.stop()