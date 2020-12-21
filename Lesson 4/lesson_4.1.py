from sys import argv


try:
    script_name, output, rate, premium = argv
    print(f'Выработка в часах: {output}')
    print(f'Ставка в час: {rate}')
    print(f'Премия: {premium}')
    salary = float(output) * int(rate) + int(premium)
    print(f'Заработная плата сотрудника: {salary:02}')
except ValueError:
    print('Неверный формат либо недостаточное число параметров')
