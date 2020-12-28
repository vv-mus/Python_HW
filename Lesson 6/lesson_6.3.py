class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):
    def get_full_name(self):
        print(f'Имя: {self.name}\nФамилия: {self.surname}')

    def get_total_income(self):
        print(f'Доход с учетом премии: {sum(self._income.values())}')


worker = Position('Иван', 'Иванов', 'рабочий', 30000, 10000)
worker.get_full_name()
print(f'Должность: {worker.position}')
worker.get_total_income()
