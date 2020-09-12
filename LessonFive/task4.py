rus_numb_dict = {
    1: 'Один',
    2: 'Два',
    3: 'Три',
    4: 'Четыре',
}
print('Получаем записи из файла task4_englishSample.txt:\n')
try:
    with open(r'task4_englishSample.txt', 'r') as f_o:
        numb_dict = {}
        while True:
            content = f_o.readline()
            if not content:
                break
            print(content, end='')
            content = content.replace('\n','')
            line_list = content.split(" ")
            line_list.remove('-')
            numb_dict[rus_numb_dict.get(int(line_list[1]))] = int(line_list[1])
except FileNotFoundError:
    print('Произошла ошибка "Файл не найден" на этапе чтения строк из файла.')
    with open(r'task4_errors.txt', 'w') as log_file:
        print('A FileNotFoundError (file not found) occurred while reading lines from a file.', file=log_file)
except IOError:
    print('Произошла ошибка ввода-вывода на этапе чтения строк из файла.')
    with open(r'task4_errors.txt', 'w') as log_file:
        print('An IOError (input / output) occurred while reading lines from a file.', file=log_file)
print('\n\nВыполняем запись в файл task4_russianSample.txt...')
error = False
try:
    with open(r'task4_russianSample.txt', 'w') as result_file:
        for key, value in numb_dict.items():
            output_content = f'{key} - {value}\n'
            result_file.write(output_content)
except IOError:
    print('Произошла ошибка ввода-вывода на этапе записи строк в файл.')
    with open(r'task4_errors.txt', 'w') as log_file:
        print('An IOError (input / output) occurred while writing lines to file.', file=log_file)
    error = True
if not error:
    print('Запись успешно выполнена.')