# task4
print("Решение четвертого задания")

big_string = input("Введите строку из нескольких слов, разделённых пробелами: ")
big_list = big_string.split(' ')
print("Строка разделена. Итог: ")
for el in range(len(big_list)):
    if len(big_list[el]) > 10:
        print(f"{el + 1}) {big_list[el][:10]}")
    else:
        print(f"{el + 1}) {big_list[el]}")
