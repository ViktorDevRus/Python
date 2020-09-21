"""
3. Реализовать программу работы с органическими клетками. Необходимо создать класс Клетка. В его конструкторе инициализировать
параметр, соответствующий количеству клеток (целое число). В классе должны быть реализованы методы перегрузки арифметических
операторов: сложение (__add__()), вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).Данные методы должны
применяться только к клеткам и выполнять увеличение, уменьшение, умножение и обычное (не целочисленное) деление клеток, соответственно.
В методе деления должно осуществляться округление значения до целого числа.
Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек двух клеток больше нуля,
иначе выводить соответствующее сообщение.
Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется как произведение количества ячеек этих двух клеток.
Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление количества ячеек этих двух клеток.
В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду. Данный метод
позволяет организовать ячейки по рядам.
Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу.
Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5. Тогда метод make_order() вернет строку: *****\n*****\n**.
Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5. Тогда метод make_order() вернет строку: *****\n*****\n*****.
"""


class OrganicCell:
    def __init__(self, cell_count: int):
        self.cell_count = cell_count

    def __str__(self):
        return '*' * self.cell_count

    def __add__(self, other):
        return OrganicCell(self.cell_count + other.cell_count)

    def __sub__(self, other):
        return OrganicCell(self.cell_count - other.cell_count) if (self.cell_count - other.cell_count) > 0 else f"Операция невыполнима: число ячеек первой клетки меньше числа ячеек второй клетки."

    def __mul__(self, other):
        return OrganicCell(self.cell_count * other.cell_count)

    def __truediv__(self, other):
        return OrganicCell(round(self.cell_count / other.cell_count))

    def make_order(self, cell_count_in_row: int):
        result_str = ''
        for cell in range(self.cell_count):
            if ((cell % cell_count_in_row) == 0) and (cell > 0):
                result_str = f'{result_str}\n*'
            else:
                result_str = f'{result_str}*'
        return f'{result_str}'


organic_cell_1_count = int(input('Укажите целое число ячеек первой клетки: '))
organic_cell_1 = OrganicCell(organic_cell_1_count)
print(f'Первая клетка: {organic_cell_1}')
organic_cell_2_count = int(input('Укажите целое число ячеек второй клетки: '))
organic_cell_2 = OrganicCell(organic_cell_2_count)
print(f'Вторая клетка: {organic_cell_2}')

print('Сложение двух клеток: ', organic_cell_1 + organic_cell_2)
print('Вычитание двух клеток: ', organic_cell_1 - organic_cell_2)
print('Умножение двух клеток: ', organic_cell_1 * organic_cell_2)
print('Деление двух клеток: ', organic_cell_1 / organic_cell_2)

order_for_organic_cell_1 = int(input('Укажите целое число для организации ячеек для первой клетки: '))
print('Организация ячеек первой клетки по рядам:')
print(organic_cell_1.make_order(order_for_organic_cell_1))
order_for_organic_cell_2 = int(input('Укажите целое число для организации ячеек для второй клетки: '))
print('Организация ячеек второй клетки по рядам:')
print(organic_cell_2.make_order(order_for_organic_cell_2))
