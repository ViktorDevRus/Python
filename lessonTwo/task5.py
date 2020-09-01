# task5
print("Решение пятого задания")
my_list = [7, 5, 3, 3, 2]
print("Исходная структура Рейтинга: ", end='')
for el in range(len(my_list)):
    if el != len(my_list) - 1:
        print(my_list[el], end=',')
    else:
        print(my_list[el])
new_element = int(input("Задайте новый элемент рейтинга: "))
while new_element < 1:
    new_element = int(input("Нужно натуральное число (от 1)! Задайте новый элемент рейтинга: "))
new_element_count = my_list.count(new_element)
new_element_index = 0
if new_element_count > 0:
    new_element_index = my_list.index(new_element)
    my_list.insert(new_element_index + new_element_count, new_element)
elif new_element_count == 0:
    final = False
    for el in range(len(my_list)):
        if new_element > my_list[el]:
            new_element_index = el
            my_list.insert(new_element_index, new_element)
            final = True
            break
    if not final:
        my_list.append(new_element)
print("Новая структура Рейтинга: ", end='')
for el in range(len(my_list)):
    if el != len(my_list) - 1:
        print(my_list[el], end=',')
    else:
        print(my_list[el])
