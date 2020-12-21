from itertools import count


begin = int(input('Введите начальное значение: '))
i = int(input('Введите последнее значение: '))
for el in count(begin):
    if el > i:
        break
    else:
        print(el)
