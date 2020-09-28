"""
1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
 В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год и
 преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и
 года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
"""


class Date:
    day: int
    month: int
    year: int

    def __init__(self, date_str: str):
        self.date = date_str

    @classmethod
    def get_day_month_year(cls, date_str: str):
        try:
            date_list = date_str.split('-')
            Date.day = int(date_list[0])
            Date.month = int(date_list[1])
            Date.year = int(date_list[2])
            return Date.day, Date.month, Date.year
        except ValueError as err:
            print(f'Неверный формат даты либо задано некорректное значение для параметра/аргумента (не число). Ошибка на этапе преобразования типов: {err}')
            

    @staticmethod
    def validate_date(param_day, param_month, param_year):
        print('Проверка данных на валидность:')
        try:
            print('День валиден (задан корректно)') if param_day in range(1, 32) and int(param_day) else print(
            'День невалиден (задан некорректно)')
            print('Месяц валиден (задан корректно)') if param_month in range(1, 13) and int(param_month) else print(
            'Месяц невалиден (задан некорректно)')
            print('Год валиден (задан корректно)') if param_year in range(1, 2101) and int(param_year) else print(
            'Год невалиден (задан некорректно)')
        except ValueError as err:
            print(f'Некорректное значение для параметра/аргумента (не число). Ошибка на этапе преобразования типов: {err}')
            
        else:
            print('Валидация завершена.')


input_date_string = input('Укажите дату формата "день-месяц-год" (день - от 1 до 31, месяц - от 1 до 12, год - от 1 до 2100): ')
my_day, my_month, my_year = Date.get_day_month_year(input_date_string)
print(f'День: {my_day}, месяц: {my_month}, год: {my_year}')
Date.validate_date(my_day, my_month, my_year)
