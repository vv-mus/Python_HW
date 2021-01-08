from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self):
        pass

    @property
    @abstractmethod
    def calc(self):
        pass


class Coat(Clothes):
    def __init__(self, v):
        super().__init__()
        self.v = v

    @property
    def calc(self):
        return (self.v / 6.5) + 0.5


class Costume(Clothes):
    def __init__(self, h):
        super().__init__()
        self.h = h

    @property
    def calc(self):
        return 2 * self.h + 0.5


v = float(input('Введите размер пальто: '))
h = float(input('Введите рост костюма: '))

coat = Coat(v)
costume = Costume(h)
print(f'Количество необходимой ткани для пошива пальто: {coat.calc:.2f} м')
print(f'Количество необходимой ткани для пошива костюма: {costume.calc:.2f} м')
print(f'Суммарный расход ткани на производство одежды: {coat.calc + costume.calc:.2f} м')
