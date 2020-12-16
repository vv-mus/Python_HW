def my_func(a,b,c):
    if a < b:
        min = a
    else:
        min = b
    if c < min:
        min = c
    res = a + b + c - min
    return res
a = int(input('Введите число A: '))
b = int(input('Введите число B: '))
c = int(input('Введите число C: '))
print(f'Сумма наибольших введенных чисел равна {my_func(a,b,c)}')
