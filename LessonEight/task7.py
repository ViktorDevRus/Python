"""
7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку методов
сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив
сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.
"""


class ComplexNumber:
    def __init__(self, first_float_number, second_float_number):
        self.first_float_number = first_float_number
        self.second_float_number = second_float_number
        self.imaginary_one = 'j'

    def __str__(self):
        first_str = ''
        second_str = ''
        if self.first_float_number.is_integer():
            first_str = str(int(self.first_float_number))
        else:
            first_str = str(self.first_float_number)
        if self.second_float_number.is_integer():
            second_str = str(int(self.second_float_number))
        else:
            second_str = str(self.second_float_number)
        return f'({first_str}+{second_str}{self.imaginary_one})'

    def __add__(self, other):
        return ComplexNumber(self.first_float_number + other.first_float_number,
                             self.second_float_number + other.second_float_number)

    def __mul__(self, other):
        result_first_float_number = (self.first_float_number * other.first_float_number) - (
                    self.second_float_number * other.second_float_number)
        result_second_float_number = (self.first_float_number * other.second_float_number) + (
                    self.second_float_number * other.first_float_number)
        return ComplexNumber(result_first_float_number, result_second_float_number)


complex_input = input('Укажите действительные числа a и b для первого комплексного числа вида (a + bj) через пробел: ')
complex_input_list = complex_input.split(' ')
complex_number_one = ComplexNumber(first_float_number=float(complex_input_list[0]),
                                   second_float_number=float(complex_input_list[1]))
complex_internal_one = complex(float(complex_input_list[0]), float(complex_input_list[1]))
print(f'Получили первое комплексное число: {complex_number_one}')
complex_input = input('Укажите действительные числа c и d для второго комплексного числа вида (с + dj) через пробел: ')
complex_input_list = complex_input.split(' ')
complex_number_two = ComplexNumber(first_float_number=float(complex_input_list[0]),
                                   second_float_number=float(complex_input_list[1]))
complex_internal_two = complex(float(complex_input_list[0]), float(complex_input_list[1]))
print(f'Получили второе комплексное число: {complex_number_two}')
print('Сумма заданных комплексных чисел равна: ', complex_number_one + complex_number_two)
print('Проверка результата суммы со встроенной функцией сложения комплексных чисел: ',
      complex_internal_one + complex_internal_two)
print('Результат умножения заданных комплексных чисел: ', complex_number_one * complex_number_two)
print('Проверка результата умножения со встроенной функцией умножения комплексных чисел: ',
      complex_internal_one * complex_internal_two)
