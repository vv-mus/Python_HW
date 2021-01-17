class NumError(Exception):
    def __init__(self, txt):
        self.txt = txt


list_num = []
while True:
    try:
        el = input('Введите число, для выхода введите "stop": ').lower()
        if el == 'stop':
            print(f'Вы ввели следующие числа: {list_num}')
            break
        elif el.isnumeric():
            list_num.append(int(el))
        else:
            raise NumError('Вы ввели не число!')
    except NumError as err:
        print(err)
