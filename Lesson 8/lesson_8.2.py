class ZeroError(Exception):
    def __init__(self, txt):
        self.txt = txt


try:
    dividend = int(input('Введите делимое (целое число): '))
    divider = int(input('Введите делитель (целое число): '))
    if divider == 0:
        raise ZeroError('На 0 делить нельзя!')
except ValueError:
    print('Вы ввели не целое число!')
except ZeroError as err:
    print(err)
else:
    print(f'Частное {dividend} и {divider} равно {dividend / divider}')
