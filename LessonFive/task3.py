print('Получаем записи сотрудников из файла:\n')
try:
    with open(r'task3_sample.txt', 'r') as f_o:
        staff_dict = {}
        f_o.seek(16)
        staff_count = 0
        while True:
            content = f_o.readline()
            if content == 'end':
                break
            print(content, end='')
            line_list = content.split(" ")
            staff_dict[line_list[0][:-1]] = int(line_list[1][:-1])
            staff_count += 1
except FileNotFoundError:
    print('Произошла ошибка "Файл не найден" на этапе чтения строк из файла.')
    with open(r'task3_errors.txt', 'w') as log_file:
        print('A FileNotFoundError (file not found) occurred while reading lines from a file.', file=log_file)
except IOError:
    print('Произошла ошибка ввода-вывода на этапе чтения строк из файла.')
    with open(r'task3_errors.txt', 'w') as log_file:
        print('An IOError (input / output) occurred while reading lines from a file.', file=log_file)
print('\nСотрудники с зарплатой меньше 20 000 рублей: ')
for key, value in staff_dict.items():
    if value < 20000:
        print(key)
sum_salary = 0
for salary in staff_dict.values():
    sum_salary += salary
print(f'\n Средняя величина дохода сотрудников, рублей: {round(sum_salary/staff_count, 2)}')