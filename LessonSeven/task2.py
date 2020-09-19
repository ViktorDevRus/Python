"""
2. Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта —
 одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм. У этих типов
 одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3).
Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы
для основных классов проекта, проверить на практике работу декоратора @property.
"""


class Dress:
    def __init__(self, title: str):
        self.title = title

    def calculation_of_tissue_consumption(self):
        pass


class Coat(Dress):
    def __init__(self, title: str, v: int):
        super().__init__(title)
        self.__size = v

    @property
    def size(self):
        return f'Размер у {self.title}: {self.__size}'

    def calculation_of_tissue_consumption(self):
        return round(self.__size / 6.5 + 0.5, 2)


class Suit(Dress):
    def __init__(self, title: str, h: int):
        super().__init__(title)
        self.__height = h

    @property
    def height(self):
        return f'Рост у {self.title}: {self.__height}'

    def calculation_of_tissue_consumption(self):
        return round(self.__height * 2 + 0.3, 2)


my_coat_size = int(input('Задайте размер вашего пальто: '))
my_coat = Coat('Пальто', my_coat_size)

my_suit_height = int(input('Задайте рост вашего костюма: '))
my_suit = Suit('Костюм', my_suit_height)
print(f'Расчет суммарного расхода ткани на производство одежды ({my_coat.size}; {my_suit.height}): {my_coat.calculation_of_tissue_consumption() + my_suit.calculation_of_tissue_consumption()}')
