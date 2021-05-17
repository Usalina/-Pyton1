#Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата
# «день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod,
# должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года
# (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.

class Data:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year
        print(f' дата: ', '%02d' % day, ':', '%02d' % month, ':', year)


    @staticmethod
    def data_static(day, month, year):
        print(f' дата: ', '%02d' % day, ':', '%02d' % month, ':', year)


    @classmethod
    def data_metod(cls, day, month, year):
        print(f' дата: ', '%02d' % day, ':', '%02d' % month, ':', year)

a = Data(1, 1, 2011)
b = Data.data_static(2, 3, 2004)
c = Data.data_metod(4, 11, 2021)

# Я наверно опять не поняла задание


