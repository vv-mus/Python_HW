class Store:
    def __init__(self, number, square, capacity, fullness=0):
        self.store = {'Принтеры': {},
                      'Сканеры': {},
                      'Копировальные аппараты': {}
                      }
        self.num = number
        self.capacity = capacity
        self.fullness = fullness
        self.square = square

    def __str__(self):
        return f'Склад № {self.num}:\nПлощадь: {self.square}\nВместимость: {self.capacity}\n' \
               f'Заполненность: {self.fullness}'

    def add_item(self, item):
        if item.num <= self.capacity - self.fullness:
            self.store[item.type_tech].update(item.tech)
            self.fullness += item.num
        else:
            print('Склад заполнен!')

    def sale_item(self, item, amount):
        self.store[item.type_tech][item.model] -= amount
        self.fullness -= amount


class OfficeEquipment:
    def __init__(self, type_tech, amount):
        self.type_tech = type_tech
        self.num = amount


class Printer(OfficeEquipment):
    def __init__(self, type_tech, amount, model_tech):
        super().__init__(type_tech, amount)
        self.model = model_tech
        self.tech = {model_tech: amount}


class Scanner(OfficeEquipment):
    def __init__(self, type_tech, amount, model_tech):
        super().__init__(type_tech, amount)
        self.model = model_tech
        self.tech = {model_tech: amount}


class Copier(OfficeEquipment):
    def __init__(self, type_tech, amount, model_tech):
        super().__init__(type_tech, amount)
        self.model = model_tech
        self.tech = {model_tech: amount}


store = Store(1, 100, 100)
while True:
    print('Меню\n1. Добавить принтер на склад\n2. Добавить сканер на склад\n3. Добавить копировальный аппарат на '
          'склад\n4. Продать принтер\n5. Продать сканер\n6. Продать копировальный аппарат\n7. Показать товары на '
          'складе\n8. Информация о складе\n9. Выход')
    user_answer = input('Выберите действие: ')
    if user_answer in ['1', '2', '3']:
        try:
            num = int(input('Введите количество: '))
        except ValueError:
            print('Неверный формат!')
            continue
        model = input('Введите модель: ')
        if user_answer == '1':
            store.add_item(Printer('Принтеры', num, model))
        elif user_answer == '2':
            store.add_item(Scanner('Сканеры', num, model))
        elif user_answer == '3':
            store.add_item(Copier('Копировальные аппараты', num, model))
    elif user_answer in ['4', '5', '6']:
        try:
            num = int(input('Введите количество: '))
        except ValueError:
            print('Неверный формат!')
            continue
        model = input('Введите модель: ')
        if user_answer == '4':
            store.sale_item(Printer('Принтеры', num, model), num)
        elif user_answer == '5':
            store.sale_item(Scanner('Сканеры', num, model), num)
        elif user_answer == '6':
            store.sale_item(Copier('Копировальные аппараты', num, model), num)
    elif user_answer == '7':
        print(f'Товары на складе:\n{store.store}')
    elif user_answer == '8':
        print(store)
    elif user_answer == '9':
        break
    else:
        print('Неверный ввод!')
        continue
