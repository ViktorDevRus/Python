print('Решение пятого задания')
print('Программа считает сумму введенных чисел, введенных через пробел.')
print('Если при вводе чисел вы вместо числа укажете символ "Q" или "q", ', end='')
print('то программа будет завершена и будет выведена сумма чисел до ввода "Q" или "q"')


def sum_num_str(num_string):
    num_list = num_string.split(' ')
    summa = 0
    final = False
    for el in range(len(num_list)):
        if num_list[el] == 'Q' or num_list[el] == 'q':
            final = True
            break
        else:
            num_list[el] = int(num_list[el])
            summa = summa + num_list[el]
    return summa, final


agreement = True
result = 0
while agreement:
    num_str = input('Задайте строку чисел, разделенных пробелом: ')
    sum_str, final_of_program = sum_num_str(num_str)
    result = result + sum_str
    print(f'Сумма всех введенных чисел: {result}')
    if final_of_program:
        break
    agreement = input('Продолжить ввод чисел? y- Да, n - Нет: ')
    agreement = True if agreement == 'y' else False
