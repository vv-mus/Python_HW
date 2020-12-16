start = float(input('Сколько Вы пробежали километров в первый день? '))
finish = float(input('Какого результата Вы хотите добиться? '))
day = 1
if start >= finish:
    print('Вы уже достигли нужного результата.')
else:
    while start < finish:
        start = start + start * 0.1
        day += 1
    print(f'Вы достигнете требуемого результата на {day} день.')