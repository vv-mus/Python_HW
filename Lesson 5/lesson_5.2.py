with open('Data\\5.2.txt', 'r', encoding='UTF-8') as file:
    words = 0
    for line, word in enumerate(file.readlines()):
        words += len(word.split())
        print(f'Номер строки: {line + 1}\nКоличество слов: {len(word.split())}\n')
    print(f'Количество строк в файле: {line + 1}, слов: {words}')
