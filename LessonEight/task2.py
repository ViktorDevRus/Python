"""
2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
 вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту
 ситуацию и не завершиться с ошибкой.
"""


class DivByZero(Exception):
    def __init__(self, txt):
        self.txt = txt


dividend = int(input('Укажите делимое (число): '))
divider = int(input('Укажите делитель (число): '))
result = 1.0
try:
    if divider == 0:
        raise DivByZero('Вы ввели ноль для делителя: деление на ноль запрещено!')
    result = dividend / divider
except DivByZero as error_obj:
    print(error_obj.txt)
else:
    print(f"Результат деления: {result}")
finally:
    print("Программа завершена.")
