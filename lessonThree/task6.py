print('Решение шестого задания')


def int_func(low_str: str):
    result = low_str.capitalize()
    return result


low_word = input('Введите слово из маленьких латинских букв: ')
upper_first_letter_word = int_func(low_word)
print(f'Результат - слово с прописной первой буквой: {upper_first_letter_word}')

print('Окей, идём дальше! Теперь нужно ввести строку из слов, разделенных пробелом.')
print('Каждое слово должно состоять из латинских букв в нижнем регистре: ')
low_string = input()
low_list = low_string.split(' ')
print('Результат: ', end='')
for word in list(map(int_func, low_list)):
    print(word, end=' ')
