from functools import reduce


def my_func(prev_el, el):
    return prev_el * el


my_list = [el for el in range(100, 1001, 2)]
print("Исходный список:", my_list)
result = reduce(my_func, my_list)
print(f"Результат вычисления произведения всех элементов списка: {result}")
