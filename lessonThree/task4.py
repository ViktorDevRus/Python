print('Решение четвертого задания')


def my_func(x, y):
    result1 = x ** y
    result2 = 1
    while y < 0:
        result2 = result2 * x
        y += 1
    result2 = 1 / result2
    return result1, result2


try:
    x_num = int(input('Укажите действительное положительное число x: '))
    while x_num <= 0:
        x_num = int(input('Неправильное значение! Укажите действительное положительное число x: '))
    y_num = int(input('Укажите целое отрицательное число y: '))
    while y_num >= 0:
        y_num = int(input('Неправильное значение! Укажите целое отрицательное число y: '))
    result_first, result_second = my_func(x=x_num, y=y_num)
    print(f'Результат возведения x в степень y (1-й способ): {result_first}')
    print(f'Результат возведения x в степень y (2-й способ): {result_second}')
except ValueError:
    print('Ошибка значения аргумента!')
