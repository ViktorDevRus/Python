print("Решение первого задания")


def div_func(dividend: int, divider: int):
    result = None
    try:
        result = dividend / divider
    except ZeroDivisionError as error:
        print("Ошибка деления на ноль: ", error)
    return result


first_num = 1
second_num = 1
try:
    first_num = int(input("Задайте целое число для делимого: "))
    second_num = int(input("Задайте целое число для делителя: "))
    final = div_func(first_num, second_num)
    print(f"Результат деления {first_num} на {second_num}: {final}")
except ValueError:
    print("Ошибка значения аргумента(ов)!")

