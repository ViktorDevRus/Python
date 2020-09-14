"""
5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами. Программа должна
подсчитывать сумму чисел в файле и выводить ее на экран.
"""
from random import randint
from functools import reduce


def sum_func(number_cur, number_next):
    return number_cur + number_next


int_list = [5, 7, 4, 9, 15, 8, 2, 12, 3, 11]
random_int_list = [str(el * randint(1, 10)) for el in int_list]
random_int_string = ' '.join(random_int_list)
print(f'Сгенерированы случайные числа:\n{random_int_string}')
print('\nВыполняем запись случайного набора чисел в файл task5_Sample.txt...')
error = False
try:
    with open(r'task5_Sample.txt', 'w') as numb_file:
        numb_file.write(random_int_string)
except IOError:
    print('Произошла ошибка ввода-вывода на этапе записи строк в файл.')
    with open(r'task5_errors.txt', 'w') as log_file:
        print('An IOError (input / output) occurred while writing lines to file.', file=log_file)
    error = True
if not error:
    print('Запись в файл task5_Sample.txt успешно выполнена.')
print('\nВыполняем чтение набора чисел из файла task5_Sample.txt. Числа в файле:')
try:
    with open(r'task5_Sample.txt', 'r') as read_numb_file:
        content = read_numb_file.readline()
        print(content, end='')
        numb_list = content.split(" ")
        numb_list = {int(el) for el in numb_list}
        result = reduce(sum_func, numb_list)
except FileNotFoundError:
    print('Произошла ошибка "Файл не найден" на этапе чтения строк из файла.')
    with open(r'task5_errors.txt', 'w') as log_file:
        print('A FileNotFoundError (file not found) occurred while reading lines from a file.', file=log_file)
except IOError:
    print('Произошла ошибка ввода-вывода на этапе чтения строк из файла.')
    with open(r'task5_errors.txt', 'w') as log_file:
        print('An IOError (input / output) occurred while reading lines from a file.', file=log_file)
print(f'\n\nСумма чисел в файле: {result}')
