#fifth task
print("Решение пятого задания")

cash_proceeds = float(input("Введите значение денежной выручки: "))
while cash_proceeds < 0:
    cash_proceeds = float(input("Нужно неотрицательное значение! Введите значение денежной выручки: "))
costs = float(input("Введите значение издержек/расходов: "))
while costs < 0:
    costs = float(input("Нужно неотрицательное значение! Введите значение издержек/расходов: "))
result = cash_proceeds - costs
if result > 0:
    print("Финансовый результат работы фирмы: Прибыль = {:.2f}".format(result))
    print("Рентабельность выручки: {:.2f}".format(result / cash_proceeds), ", {:.0f} процентов.".format((result / cash_proceeds) * 100))
    employees_count = int(input("Введите численность сотрудников фирмы: "))
    while employees_count <= 0:
        employees_count = float(input("Нужно положительное значение! Введите численность сотрудников фирмы: "))
    print("Прибыль фирмы в расчете на одного сотрудника: {:.2f}".format(result/employees_count))
elif result < 0:
    print("Финансовый результат работы фирмы: Убыток = {:.2f}".format(result))
elif result == 0:
    print("Финансовый результат работы фирмы: Вы сработали в ноль, прибыли/убытка нет.")