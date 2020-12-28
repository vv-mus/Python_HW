from time import sleep


class TrafficLight:
    __color = {'Красный': 7, 'Желтый': 2, 'Зеленый': 7}

    def running(self):
        for el, t in self.__color.items():
            print(f'Цвет светофора: {el}')
            sleep(t)


traffic_light = TrafficLight()
traffic_light.running()
