#fourth task
print("Решение четвертого задания")
number = int(input("Задайте целое положительное число n: "))
while number <= 0:
    number = int(input("Нужно целое положительное число! Укажите число n: "))
print("1 Способ")
curr_big_num = number // 10
max_num_one = number % 10
while curr_big_num > 0:
    if curr_big_num % 10 >= 0:
        next_num = curr_big_num % 10
    else:
        next_num = curr_big_num
    if next_num > max_num_one:
        max_num_one = next_num
    curr_big_num = curr_big_num // 10
print("Самая большая цифра в числе n: ", max_num_one)

print("2 Способ")
stroka = str(number)
leng = len(stroka)
max_num_two = int(stroka[0])
i = 0
while i < (leng - 1):
    next_num = int(stroka[i+1])
    if next_num > max_num_two:
        max_num_two = next_num
    i += 1
print("Самая большая цифра в числе n: ", max_num_two)