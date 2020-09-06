#third task
print("Решение третьего задания")

number = int(input("Задайте целое неотрицательное число n: "))
while number < 0:
    number = int(input("Нужно неотрицательное число! Укажите число n: "))
stroka = f"{number}{number}"
result = number + int(stroka)
stroka = f"{number}{number}{number}"
result = result + int(stroka)
print("Результат суммы чисел n + nn + nnn равен: ", result)