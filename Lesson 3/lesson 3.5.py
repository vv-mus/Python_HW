def total(sum,b):
    while b:
        print('Для выхода введите #')
        enter = input('Введите числа через пробел: ').split()
        for el in enter:
            if el == '#':
                b = False
                break
            sum += int(el)
        print('Cумма введенных чисел:', sum)
total(0, True)
