"""
7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджеры контекста.
"""
import json

print('Обрабатываем данные фирм из файла task7_sample.txt:\n')
try:
    with open(r'task7_sample.txt', 'r', encoding='UTF-8') as read_file:
        firm_dict = {}
        firm_losses = {}
        profit_count = 0
        sum_profit = 0
        while True:
            content = read_file.readline()
            if not content:
                break
            print(content, end='')
            firm_list = content.split()
            firm_profit = int(firm_list[2]) - int(firm_list[3])
            if firm_profit > 0:
                print(f'Прибыль фирмы {firm_list[0]}: {firm_profit}')
                firm_dict[firm_list[0]] = firm_profit
                profit_count += 1
                sum_profit += firm_profit
            elif firm_profit < 0:
                print(f'Убытки фирмы {firm_list[0]}: {firm_profit}')
                firm_losses[firm_list[0]] = firm_profit
            else:
                print(f'Фирма {firm_list[0]} сработала в 0')
except FileNotFoundError:
    print('Произошла ошибка "Файл не найден" на этапе чтения строк из файла.')
    with open(r'task7_errors.txt', 'w') as log_file:
        print('A FileNotFoundError (file not found) occurred while reading lines from a file.', file=log_file)
except IOError:
    print('Произошла ошибка ввода-вывода на этапе чтения строк из файла.')
    with open(r'task7_errors.txt', 'w') as log_file:
        print('An IOError (input / output) occurred while reading lines from a file.', file=log_file)
average_profit = round(sum_profit / profit_count)
average_profit_dict = {
    'average_profit': average_profit
}
print(f'Средняя прибыль компаний: {average_profit}')
result_list = [firm_dict, firm_losses, average_profit_dict]
print(f'\nРезультирующий список: {result_list}\n')
print('Записываем данные обработки в файл task7.json...')
error = False
try:
    with open(r'task7.json', 'w') as json_file:
        json.dump(result_list, json_file)
except IOError:
    print('Произошла ошибка ввода-вывода на этапе записи строк в файл.')
    with open(r'task7_errors.txt', 'w') as log_file:
        print('An IOError (input / output) occurred while writing lines to file.', file=log_file)
    error = True
if not error:
    print('Запись успешно выполнена.')