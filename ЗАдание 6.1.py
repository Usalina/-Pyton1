#Что то я совсем не поняла задания

#1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет)
# и метод running (запуск). Атрибут реализовать как приватный.
# В рамках метода реализовать переключение светофора в режимы:
# красный, желтый, зеленый. Продолжительность первого состояния (красный) составляет 7 секунд,
# второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
# Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.

class TrafficLight:

    def __init__(self, colors, running):
        self.colors = colors
        self.__running = running

red=TrafficLight('Красный', 'горит 7 секунд')
yellow=TrafficLight('Желтый', 'горит 2 секунды')
green=TrafficLight('Зеленый', 'горит 15 секунд')
print(red.colors, red._TrafficLight__running)
print(yellow.colors, yellow._TrafficLight__running)
print(green.colors, green._TrafficLight__running)
