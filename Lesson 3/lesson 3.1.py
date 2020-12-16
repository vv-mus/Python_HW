def div(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return '\nОшибка: "На 0 делить нельзя!"'
a = int(input('Введите число № 1 (делимое): '))
b = int(input('Введите число № 2 (делитель): '))
print(f'Частное чисел {a} и {b} равно {div(a,b)}')
