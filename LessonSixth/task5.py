"""
5. Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и метод draw (отрисовка).
 Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
 В каждом из классов реализовать переопределение метода draw. Для каждого из классов методы должен выводить уникальное сообщение.
 Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
"""

class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        str = 'Запуск отрисовки: рисую'
        return str

class Pen(Stationery):
    def draw(self):
        pen_str = f'{super().draw()} ручкой.'
        print(pen_str)
        return pen_str

class Pencil(Stationery):
    def draw(self):
        pencil_str = f'{super().draw()} карандашом.'
        print(pencil_str)
        return pencil_str

class Handle(Stationery):
    def draw(self):
        handle_str = f'{super().draw()} маркером.'
        print(handle_str)
        return handle_str

my_pen = Pen('Ручка')
my_pen.draw()

my_pencil = Pencil('Карандаш')
my_pencil.draw()

my_handle = Handle('Маркер')
my_handle.draw()