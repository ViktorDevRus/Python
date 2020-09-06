def my_func(var_1, var_2, var_3):
    var_list = [var_1, var_2, var_3]
    var_list.remove(min(var_list))
    return sum(var_list)


try:
    first_arg = int(input('Первый аргумент: '))
    second_arg = int(input('Второй аргумент: '))
    third_arg = int(input('Третий аргумент: '))
    result = my_func(first_arg, second_arg, third_arg)
    print(f'Сумма наибольших двух аргументов: {result}')
except ValueError:
    print('Ошибка значения аргумента!')
