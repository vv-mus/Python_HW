amount = int(input('Введите количество элементов списка: '))
num = 0
list = []
while amount > 0:
    list.append(input(f'Введите значение элемента № {num}: '))
    amount -= 1
    num += 1
print('Первоначальный список:', list)
for i in range(1, len(list), 2):
    list[i], list[i - 1] = list[i - 1], list[i]
print('Отредактированный список:', list)