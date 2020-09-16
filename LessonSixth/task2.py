"""
2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина). Значения данных
атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными. Определить метод расчета
массы асфальта, необходимого для покрытия всего дорожного полотна. Использовать формулу: длина * ширина * масса асфальта
для покрытия одного кв метра дороги асфальтом, толщиной в 1 см * чи сло см толщины полотна. Проверить работу метода.
Например: 20м * 5000м * 25кг * 5см = 12500 т
"""


class Road:
    asphalt_mass_kvm_per_centimeter_height = 25
    centimeter_height = 5

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def asphalt_mass_calculation(self):
        result = (self._length * self._width * Road.asphalt_mass_kvm_per_centimeter_height * Road.centimeter_height) / 1000
        print(f'Масса асфальта, необходимого для покрытия всего дорожного полотна, тонн: {result}')
        return result


road_length = 0
road_width = 0
try:
    road_length = int(input('Укажите длину дороги: '))
    road_width = int(input('Укажите ширину дороги: '))
except ValueError:
    print('Ошибка на этапе задания аргументов!')
    with open(r'errors.txt', 'w') as log_file:
        print('A ValueError occurred while setting params for Object Road.', file=log_file)

road_obj = Road(road_length, road_width)
road_obj.asphalt_mass_calculation()
