print('Введите построчно данные в файл (пустая строка - окончание ввода): ')
try:
    with open(r'task1_user_input.txt', 'w') as f_o:
        while True:
            string = input()
            if string != '':
                string = f'{string}\n'
                f_o.write(string)
            else:
                break
except IOError:
    print('Произошла ошибка ввода-вывода на этапе создания файла и записи строк в файл.')
    with open(r'errors.txt', 'w') as log_file:
        print('An IOError (input / output) error occurred during the file creation phase and writing lines to the file.', file=log_file)
print('Получаем (проверяем) строки из файла: ')
try:
    with open(r'task1_user_input.txt', 'r') as f_o:
        for line in f_o:
            print(line, end='')
except FileNotFoundError:
    print('Произошла ошибка "Файл не найден" на этапе чтения строк из файла.')
    with open(r'errors.txt', 'w') as log_file:
        print('A FileNotFoundError (file not found) occurred while reading lines from a file.', file=log_file)
except IOError:
    print('Произошла ошибка ввода-вывода на этапе чтения строк из файла.')
    with open(r'errors.txt', 'w') as log_file:
        print('An IOError (input / output) occurred while reading lines from a file.', file=log_file)