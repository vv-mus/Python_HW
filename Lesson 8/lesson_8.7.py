class Complex:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return f'(Комплексное число: {self.a} + {self.b}i)'

    def __add__(self, other):
        return Complex(self.a + other.a, self.b + other.b)

    def __mul__(self, other):
        return Complex(self.a * other.a - self.b * other.b, self.a * other.b + self.b * other.a)


c1 = Complex(7, -1)
c2 = Complex(3, 1)
print(c1)
print(c2)
print(f'Сумма: {c1 + c2}')
print(f'Произведение: {c1 * c2}')
