#Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
# размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
#Для определения расхода ткани по каждому типу одежды использовать формулы:
# для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3).
# Проверить работу этих методов на реальных данных.
#Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

class Costume:

    def __init__(self, name, height):
        self.name = name
        self.height = height

    @property
    def tissue_consumption(self):
        return round(2 * self.height + 0.3, 2)

    def __add__(self, other):
        return self.tissue_consumption + other.tissue_consumption


class Coat:

    def __init__(self, name, size):
        self.name = name
        self.size = size

    @property
    def tissue_consumption(self):
        return round(self.size / 6.5 + 0.5, 2)

    def __add__(self, other):
        return self.tissue_consumption + other.tissue_consumption


costume = Costume('костюм', 1.78)
print(costume.name)
print(costume.tissue_consumption)

coat = Coat('пальто', 40)
print(coat.name)
print(coat.tissue_consumption)

print(costume + coat)
