def fact(number):
    if number == 0:
        yield 1
    factorial = 1
    while number > 1:
        factorial *= number
        number -= 1
    for num in range(1, factorial + 1):
        yield num


n = 1
try:
    n = int(input("Введите целое число n: "))
except ValueError:
    print('Ошибка задания аргумента!')
n = abs(n)
if n != 0:
    print(f"[ВЫВОД ДЛЯ КОНТРОЛЯ]Числа от 1! и до {n}! :", end=' ')
    for el in fact(n):
        print(el, end=' ')
    print()
    print(f'Вывод  первых {n} чисел, начиная с 1! и до {n}! :', end=' ')
    i = 1
    for el in fact(n):
        if i <= n:
            print(el, end=' ')
            i += 1
else:
    print(f'Вывод  первых {n} чисел, начиная с 1! и до {n}! :', None)
