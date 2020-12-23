with open('Data\\5.5.txt', 'w', encoding='UTF-8') as file:
    file.write(input('Введите числа через пробел: '))
with open('Data\\5.5.txt', 'r', encoding='UTF-8') as file:
    num = file.read()
    num = num.split()
    s = 0
    for i in range(len(num)):
        s += int(num[i])
    print(f'Сумма введеных чисел равна {s}')
