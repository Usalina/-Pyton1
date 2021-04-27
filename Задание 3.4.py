#Хотела сделать так, чтобы числа можно было вводить и отрицательные и положительные, но что то затупила

x=int(input('Введите число1: '))
y=int(input('Введите число2 (отрицательное): '))

def my_func(x, y):
    return (round(x**y, 5))

print(my_func(x, y))

def my_func2(x, y):
    return (round(1/x1, 5))

x1=x
for i in range(abs(y)-1):
    x1=(x1*x)
print(my_func2(x, y))
