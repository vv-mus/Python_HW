t = int(input('Введите количество секунд: '))
h = t // 3600
m = (t - h*3600) // 60
s = t-(h*3600 + m * 60)
print(f'{t} сек.:\n{h} ч. : {m} мин. : {s} сек.')