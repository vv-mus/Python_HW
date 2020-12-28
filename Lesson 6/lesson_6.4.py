from time import sleep


class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'Автомобиль: {self.name}. Действие: автомобиль поехал')
        sleep(2)

    def stop(self):
        print(f'Автомобиль: {self.name}. Действие: автомобиль остановился')
        sleep(2)

    def turn(self, direction):
        print(f'Автомобиль: {self.name}. Действие: автомобиль повернул {direction}')
        sleep(2)

    def show_speed(self):
        print(f'Автомобиль: {self.name}. Скорость автомобиля: {self.speed}')
        sleep(2)


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'Автомобиль: {self.name}. Превышение скорости!')
            sleep(2)
        else:
            super().show_speed()


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'Автомобиль: {self.name}. Превышение скорости!')
            sleep(2)
        else:
            super().show_speed()


class SportCar(Car):
    def show_speed(self):
        if self.speed > 120:
            print(f'Автомобиль: {self.name}. Превышение скорости!')
            sleep(2)
        else:
            super().show_speed()


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=True):
        super().__init__(speed, color, name, is_police)


town_car = TownCar(50, 'Черный', 'Городской автомобиль')
town_car.go()
town_car.turn('налево')
town_car.turn('направо')
town_car.show_speed()
town_car.stop()

work_car = WorkCar(90, 'Белый', 'Рабочий автомобиль')
work_car.go()
work_car.turn('налево')
work_car.turn('направо')
work_car.show_speed()
work_car.stop()

sport_car = SportCar(160, 'Желтый', 'Спортивный автомобиль')
sport_car.go()
sport_car.turn('налево')
sport_car.turn('направо')
sport_car.show_speed()
sport_car.stop()

police_car = PoliceCar(80, 'Комбинированный', 'Полицейский автомобиль')
police_car.go()
police_car.turn('налево')
police_car.turn('направо')
police_car.show_speed()
police_car.stop()
