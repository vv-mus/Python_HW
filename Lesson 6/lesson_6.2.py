class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def mass_calculation(self):
        mass = (self._length * self._width * 25 * 5) / 1000
        print(f'Масса асфальта: {mass:.2f} т')


road = Road(float(input('Введите длину дороги в метрах: ')), float(input('Введите ширину дороги в метрах: ')))
road.mass_calculation()
