from itertools import count

for el in count(3):
    if el > 10:
        break
    else:
        print(el)
