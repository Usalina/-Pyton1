#Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
#Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
#Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица.


class Matrix:

    def __init__(self, data11, data12, data13, data21, data22, data23, data31, data32, data33):
        self.data11 = data11
        self.data12 = data12
        self.data13 = data13
        self.data21 = data21
        self.data22 = data22
        self.data23 = data23
        self.data31 = data31
        self.data32 = data32
        self.data33 = data33


    def __str__(self):
        return f'{self.data11}, {self.data12}, {self.data13}, {self.data21}, {self.data22}, {self.data23}, {self.data31}, {self.data32}, {self.data33}'

    def __add__(self, other):
        return Matrix(self.data11 + other.data11, self.data12 + other.data12, self.data13 + other.data13,
                      self.data21 + other.data21, self.data22 + other.data22, self.data23 + other.data23,
                      self.data31 + other.data31, self.data32 + other.data32, self.data33 + other.data33)



import random

one = Matrix(random.randint(1, 9), random.randint(1, 9), random.randint(1, 9), random.randint(1, 9), random.randint(1, 9), random.randint(1, 9), random.randint(1, 9), random.randint(1, 9), random.randint(1, 9))
print(one)

two = Matrix(random.randint(1, 9), random.randint(1, 9), random.randint(1, 9), random.randint(1, 9), random.randint(1, 9), random.randint(1, 9), random.randint(1, 9), random.randint(1, 9), random.randint(1, 9))
print(two)

print(one + two)
