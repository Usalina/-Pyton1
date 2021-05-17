#Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.”
# Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
# В каждом из классов реализовать переопределение метода draw. Для каждого из классов методы должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return 'Запуск отрисовки'

class Pen(Stationery):

    def draw(self):
        return 'синяя ручка'

class Pencil(Stationery):

    def draw(self):
        return 'черный карандаш'

class Handle(Stationery):

    def draw(self):
        return 'красный маркер'


tassel = Stationery('кисть')
print(tassel.draw())

pen = Pen('ручка')
print(pen.title, pen.draw())

pencil = Pencil('карандаш')
print(pencil.title, pencil.draw())

handle = Handle('маркер')
print(handle.title, handle.draw())