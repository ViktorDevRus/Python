"""
6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого предмета не обязательно
были все типы занятий. Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
Вывести словарь на экран.
"""
from functools import reduce

print('\nВыполняем чтение предметов из файла task6_Sample.txt:\n')


def clean_str(string):
    i = 0
    new_string = ''
    while i < len(string):
        if string[i] in (' ', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'):
            new_string = f'{new_string}{string[i]}'
        i += 1
    return new_string


def sum_elements(el_cur, el_next):
    return el_cur + el_next


try:
    with open(r'task6_sample.txt', 'r', encoding='UTF-8') as read_file:
        lessons_dict = {}
        while True:
            content = read_file.readline()
            if not content:
                break
            print(content, end='')
            index = content.find(':')
            lesson = content[:index]
            hours_str = content[index + 1:]
            hours_list = list(map(int, clean_str(hours_str).split()))
            hours_count = reduce(sum_elements, hours_list)
            lessons_dict[lesson] = hours_count
except FileNotFoundError:
    print('Произошла ошибка "Файл не найден" на этапе чтения строк из файла.')
    with open(r'task6_errors.txt', 'w') as log_file:
        print('A FileNotFoundError (file not found) occurred while reading lines from a file.', file=log_file)
except IOError:
    print('Произошла ошибка ввода-вывода на этапе чтения строк из файла.')
    with open(r'task6_errors.txt', 'w') as log_file:
        print('An IOError (input / output) occurred while reading lines from a file.', file=log_file)
print(f'\n\nРезультирующий словарь: {lessons_dict}')
