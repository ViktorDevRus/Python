#sixth task
print("Решение шестого задания")

result_first_day = int(input("Укажите результат первого дня, км: a = "))
result_last_day = int(input("Укажите общий результат спортсмена, км: b = "))
result_next_day = result_first_day
result_day = 1
while result_next_day < result_last_day:
    print("{} день: {:.2f}".format(result_day, result_next_day))
    result_next_day = result_next_day * 1.1
    result_day += 1
else:
    print("{} день: {:.2f}".format(result_day, result_next_day))
print("На {} день спортсмен достиг результата — не менее {} км.".format(result_day, result_last_day))