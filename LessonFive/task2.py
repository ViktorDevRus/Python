print('Получаем строки из файла:\n')
try:
    with open(r'task2_sample.txt', 'r') as f_o:
        str_count = 0
        i = 1
        words_count_dict = {}
        for line in f_o:
            print(line, end='')
            words_count_dict[i] = len(line.split(" "))
            i += 1
            str_count += 1
except FileNotFoundError:
    print('Произошла ошибка "Файл не найден" на этапе чтения строк из файла.')
    with open(r'task2_errors.txt', 'w') as log_file:
        print('A FileNotFoundError (file not found) occurred while reading lines from a file.', file=log_file)
except IOError:
    print('Произошла ошибка ввода-вывода на этапе чтения строк из файла.')
    with open(r'task2_errors.txt', 'w') as log_file:
        print('An IOError (input / output) occurred while reading lines from a file.', file=log_file)
print(f'\n\nКоличество строк в файле: {str_count}')
for key, value in words_count_dict.items():
    print(f'Количество слов в {key} строке: {value}')