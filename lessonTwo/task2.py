# task2
print("Решение второго задания")
my_list = []
size = int(input("Укажите размер списка: "))
while size <= 0:
    size = int(input("Нужно положительное целое число! Укажите размер списка: "))
print(f'Заполните список элементами')
for el in range(size):
    print(f"Элемент {el}: ", end='')
    my_list.insert(el, input())
print("Задан список: ", my_list)
i = 0
while i < (size - 1):
    my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
    i += 2
print("Произведена перестановка. Получен список: ", my_list)
