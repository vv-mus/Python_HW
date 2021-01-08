class Cell:
    def __init__(self, num):
        self.num = num

    def __add__(self, other):
        return self.num + other.num

    def __sub__(self, other):
        if self.num - other.num > 0:
            return self.num - other.num
        else:
            print('Операция вычитания невозможна!')
            return 0

    def __mul__(self, other):
        return self.num * other.num

    def __truediv__(self, other):
        return self.num // other.num

    def make_order(self, cells_in_raw):
        res = ''
        for el in range(self.num // cells_in_raw):
            res += '*' * cells_in_raw + '\n'
        res += '*' * (self.num % cells_in_raw)
        return res


raw = int(input('Введите количество отображения ячеек в клетке в одном ряду: '))
cell_1 = Cell(int(input('Введите количество ячеек в клетке № 1: ')))
cell_2 = Cell(int(input('Введите количество ячеек в клетке № 2: ')))
print(f'Исходная клетка № 1:\n{cell_1.make_order(raw)}')
print(f'Исходная клетка № 2:\n{cell_2.make_order(raw)}')
cell_3 = Cell(cell_1 + cell_2)
print(f'Результат сложения исходных клеток:\n{cell_3.make_order(raw)}')
cell_3 = Cell(cell_1 - cell_2)
print(f'Результат вычитания исходных клеток:\n{cell_3.make_order(raw)}')
cell_3 = Cell(cell_1 * cell_2)
print(f'Результат умножения исходных клеток:\n{cell_3.make_order(raw)}')
cell_3 = Cell(cell_1 / cell_2)
print(f'Результат деления исходных клеток:\n{cell_3.make_order(raw)}')
