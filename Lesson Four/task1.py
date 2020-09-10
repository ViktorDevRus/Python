from sys import argv


def employee_salary(hours, money_in_hour, bonus):
    print("Функция расчета заработной платы сотрудника")
    try:
        hours = int(hours)
        money_in_hour = float(money_in_hour)
        bonus = float(bonus)
    except ValueError:
        print("Ошибка значения аргумента(ов)!")
        return None
    print("выработка в часах: ", hours)
    print("ставка в час: ", money_in_hour)
    print("премия: ", bonus)
    result = round(hours * money_in_hour + bonus, 2)
    return result


script_name, hours_arg, money_in_hour_arg, bonus_arg = argv
salary = employee_salary(hours_arg, money_in_hour_arg, bonus_arg)
print(f"Заработная плата сотрудника: {salary}")
