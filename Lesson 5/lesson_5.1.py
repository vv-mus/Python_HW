with open('Data\\5.1.txt', 'w', encoding='UTF-8') as file:
    print('Для выхода введите пустую строку')
    while True:
        line = input('Введите строку: ')
        if line == '':
            break
        file.write(line + '\n')
