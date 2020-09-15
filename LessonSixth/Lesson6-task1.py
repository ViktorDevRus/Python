"""
1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) —
на ваше усмотрение. Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
Проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение и
завершать скрипт.
"""
from time import sleep
from itertools import cycle

class TrafficLight:
    def __init__(self, color):
        self.__color = color

    def running(self):
        lights_dict = {
            "Red": 7,
            "Yellow": 2,
            "Green": 5
        }
        iter = cycle(lights_dict.items())
        for key, value in iter:
            if key == self.__color:
                print(f"{self.__color} traffic light is on")
                sleep(value)
                second_light = next(iter)
                print(f"{second_light[0]} traffic light is on")
                sleep(second_light[1])
                third_light = next(iter)
                print(f"{third_light[0]} traffic light is on")
                sleep(third_light[1])
                break
user_color = input("Задайте начальный цвет сигнала светофора: Red - красный, Yellow - желтый, Green - зелёный: ")
while user_color not in ("Red", "Yellow", "Green"):
    user_color = input("Проверьте корректнось задания цвета {Red - красный, Yellow - желтый, Green - зелёный}! Задайте начальный цвет сигнала светофора: ")
instance_traffic_light = TrafficLight(user_color)
instance_traffic_light.running()