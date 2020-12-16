my_str = (input('Введите любую строку: ')).split()
for ind, el in enumerate(my_str):
    print(ind, el[:10])