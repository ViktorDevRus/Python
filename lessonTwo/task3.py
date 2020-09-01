# task3
print("Решение третьего задания")
month_list = [(12, 1, 2), (3, 4, 5), (6, 7, 8), (9, 10, 11)]
season_dict = {
    'Зима': month_list[0],
    'Весна': month_list[1],
    'Лето': month_list[2],
    'Осень': month_list[3]
}
month = int(input("Введите номер месяца (целое число от 1 до 12): "))
while month not in range(1, 13):
    month = int(input("Нужно целое число от 1 до 12! Введите номер месяца: "))
for el in range(len(month_list)):
    if month in month_list[el]:
        season_list = list(season_dict.keys())
        print("Указанный месяц относится к сезону: ", season_list[el])
