my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
print(f"Исходный список: {my_list}")
new_list = [my_list[el + 1] for el in range(len(my_list) - 1) if my_list[el + 1] > my_list[el]]
print(f"Новый список: {new_list}")
