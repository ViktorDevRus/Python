"""
3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker. В классе Position
реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные, проверить значения
атрибутов, вызвать методы экземпляров).
"""


class Worker:
    def __init__(self, name: str, surname: str, position: str, income: dict):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


income_dict = {
    "wage": 0,
    "bonus": 0
}


class Position:
    def __init__(self, worker_obj: Worker):
        self.worker_obj = worker_obj

    def get_full_name(self):
        full_name_str = f'{self.worker_obj.name} {self.worker_obj.surname}'
        return full_name_str

    def get_total_income(self):
        return self.worker_obj._income["wage"] + self.worker_obj._income["bonus"]


worker_name = input('Задайте имя сотрудника: ')
worker_surname = input('Задайте фамилию сотрудника: ')
worker_position = input('Укажите должность сотрудника: ')
income_dict["wage"] = int(input('Оклад сотрудника: '))
income_dict["bonus"] = int( input('Премия сотрудника: '))
worker_one = Worker(worker_name, worker_surname, worker_position, income_dict)
position_one = Position(worker_one)
print(f'Полное имя сотрудника: {position_one.get_full_name()}')
print(f'Доход сотрудника с учетом премии: {position_one.get_total_income()}')
