from itertools import cycle

c = 0
end = int(input('Введите количество повторений: '))
for el in cycle(['A', 'B', 'C']):
    if c >= end:
        break
    print(el)
    c += 1
