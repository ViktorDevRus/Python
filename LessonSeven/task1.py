"""
1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен
принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц вы найдете в методичке.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем с
первым элементом первой строки второй матрицы и т.д.
"""


class Matrix:
    def __init__(self, list_of_lists: list):
        self.matrix = list_of_lists

    def __str__(self):
        matrix_string = ''
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                matrix_string = f'{matrix_string}{str(self.matrix[i][j]):>3} '
            matrix_string = f'{matrix_string}\n'
        return matrix_string

    def __add__(self, other):
        matrix_add_result = []
        matrix_add_el_string = []
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                matrix_add_el_string.append(self.matrix[i][j] + other.matrix[i][j])
            matrix_add_result.append(matrix_add_el_string)
            matrix_add_el_string = []
        return Matrix(matrix_add_result)


my_list_1 = [[31, 22], [37, 43], [51, 86]]
my_matrix_1 = Matrix(my_list_1)
print('Первая матрица: ')
print(my_matrix_1)

my_list_2 = [[3, 5, 32], [2, 4, 6], [-1, 64, -8]]
my_matrix_2 = Matrix(my_list_2)
print('Вторая матрица: ')
print(my_matrix_2)

my_list_3 = [[3, 5, 8, 3], [8, 3, 7, 1]]
my_matrix_3 = Matrix(my_list_3)
print('Третья матрица: ')
print(my_matrix_3)

my_list_4 = [[4, 3], [3, 2], [4, 4]]
my_matrix_4 = Matrix(my_list_4)
print('Четвертая матрица: ')
print(my_matrix_4)

print('Результат сложения 1 и 4 матриц: ')
result_matrix = my_matrix_1 + my_matrix_4
print(result_matrix)