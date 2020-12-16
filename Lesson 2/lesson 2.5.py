rate = [7, 5, 3, 3, 2]
print(f'Текущий рейтинг: {rate}')
num = int(input('Введите новое значение: '))
for el in range(len(rate)):
    if num > max(rate):
        rate.insert(0, num)
        break
    elif num < min(rate):
        rate.append(num)
        break
    elif num == rate[el]:
        rate.insert(el + 1, num)
        break
    elif num < rate[el] and num > rate[el + 1]:
        rate.insert(el + 1, num)
        break
print(rate)