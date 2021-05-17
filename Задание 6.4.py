#Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
# speed, color, name, is_police (булево). А также методы: go, stop, turn(direction),
# которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
#Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
#Выполните вызов методов и также покажите результат.

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return 'машина поехала'

    def stop(self):
        return 'машина остановилась'

    def turn_right(self):
        return 'машина повернула направо'

    def turn_left(self):
        return 'машина повернула налево'

class TownCar(Car):
    def show_speed(self):
        if self.speed >= 60:
            print('скорость превышена')
        else:
            print('Скорость в пределах нормы')
        return self.speed

class SportCar(Car):
    def show_speed(self):
        return self.speed

class WorkCar(Car):
    def show_speed(self):
        if self.speed >= 40:
            print('скорость превышена')
        else:
            print('Скорость в пределах нормы')
        return self.speed

class PoliceCar(Car):
    pass

gazel = WorkCar(70, 'желтый', "Газель", None)
print(gazel.name)
print(gazel.go())
print(gazel.turn_left())
print(gazel.show_speed())
print(gazel.stop())

ford = SportCar(250, 'зеленый', 'Ford', None)
print(ford.name)
print(ford.go())
print(ford.turn_right())
print(ford.is_police)
print(ford.show_speed())

nissan = PoliceCar(80, 'белый', "Nissan", True)
print(nissan.name)
print(nissan.go())
print(nissan.turn_right())
print(nissan.is_police)
print(nissan.stop())