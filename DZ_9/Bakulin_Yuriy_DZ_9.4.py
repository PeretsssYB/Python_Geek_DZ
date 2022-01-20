# Реализуйте базовый класс Car.
# у класса должны быть следующие атрибуты: speed, color, name, is_police(bool).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar)
# и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

class Car:

    def __init__(self, speed, color, name, direction, is_police=False):
        self.speed, self.color, self.name, self.direction, self.is_police = speed, color, name, direction, is_police

    def go(self):
        print(f'{self.color} машина, марки {self.name}, поехала.')

    def stop(self):
        print(f'{self.color} машина, марки {self.name}, остановилась.')

    def turn(self):
        print(f'{self.color} машина, марки {self.name}, повернула на {self.direction}.')

    def show_speed(self):
        print(f'Текущая скорость {self.color} машины, марки {self.name}, составляет {self.speed} км/ч.')

    def police_check(self):
        if self.is_police is True:
            print(f'{self.color} машина, марки {self.name}, полицейская')
        else:
            print(f'{self.color} машина, марки {self.name}, не полицейская')


class TownCar(Car):

    def show_speed(self):
        if int(self.speed) > 60:
            print(f'{self.color} машина, марки {self.name}, превышает скорость!')
        else:
            print(f'Текущая скорость {self.color} машины, марки {self.name}, составляет {self.speed} км/ч.')


class WorkCar(Car):

    def show_speed(self):
        if int(self.speed) > 40:
            print(f'{self.color} машина, марки {self.name}, превышает скорость!')
        else:
            print(f'Текущая скорость {self.color} машины, марки {self.name}, составляет {self.speed} км/ч.')


class SportCar(Car):

    def go(self):
        print(f'{self.color} спортивная машина, марки {self.name}, стартанула с визгом.')


class PoliceCar(Car):

    def __init__(self, speed, color, name, direction):
        super().__init__(speed, color, name, direction, True)

    def go(self):
        print(f'Полицейская машина, марки {self.name}, отправилась патрулировать улицы.')


# speed, color, name, direction, is_police
car_1 = SportCar('78', 'Красная', 'Lamborgini', 'право')
car_2 = PoliceCar('50', '', 'Ford', 'право')
car_3 = TownCar('55', 'Черная', 'Волга', 'лево')
car_4 = WorkCar('38', 'Белая', 'Fiat', 'право')
car_5 = WorkCar('43', 'Белая', 'Renault', 'лево')

car_2.go(), car_1.go(), car_3.go(), car_5.go(), car_4.go()
car_2.show_speed(), car_1.show_speed(), car_3.show_speed(), car_5.show_speed(), car_4.show_speed()
car_2.police_check(), car_1.police_check(), car_3.police_check(), car_5.police_check(), car_4.police_check()
car_2.turn(), car_3.turn(), car_5.turn()
car_2.stop(), car_1.stop(), car_3.stop(), car_5.stop(), car_4.stop()
