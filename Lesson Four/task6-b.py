from itertools import cycle

cycle_list = [5, 6, 7]
print(f"Исходный список: {cycle_list}")
print("Выводим элементы циклично: ")
counter = 0
for el in cycle(cycle_list):
    if counter > 13:
        break
    else:
        print(el)
        counter += 1
