products = []
products_num = 1
msg = 'Хотите добавить первый товар в базу? (Да/Нет): '
analyze = {'Наименование товара': [], 'Цена': [], 'Количество': [], 'Единица измерения': []}
while True:
    answer = input(msg).lower()
    msg = 'Хотите добавить следующий товар в базу? (Да/Нет): '
    if answer == 'да':
        products_dict = {'Наименование товара': '', 'Цена': '', 'Количество': '', 'Единица измерения': ''}
        for key in products_dict.keys():
            products_dict[key] = input(f'Введите харакетристику "{key}": ')
            analyze[key].append(products_dict[key])
        products.append(tuple([products_num, products_dict]))
        products_num += 1
    elif answer == 'нет':
        break
print('Перечень товаров:')
for i in products:
    print(i)
print('Анализ введенных данных:')
for key in analyze:
    print(key, ':', analyze[key])