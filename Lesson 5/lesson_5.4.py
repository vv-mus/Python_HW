with open('Data/5.4.1.txt', 'r', encoding='UTF-8') as file1:
    russian = ['Один', 'Два', 'Три', 'Четыре']
    for line, word in enumerate(file1):
        num = word.split(' ')
        num[0] = russian[line]
        num = ' '.join(num)
        with open('Data/5.4.2.txt', 'a', encoding='UTF-8') as file2:
            file2.write(num)
