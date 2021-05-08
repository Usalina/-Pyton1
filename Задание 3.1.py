def my_func(arg1,arg2):
    return round(arg1 / arg2, 2)

arg1=int(input('Введите число 1: '))
arg2=int(input('Введите число 2: '))


while arg2==0:
    print('Введите другое число: ')
    arg2 = int(input('Введите число 2: '))
print(my_func(arg1, arg2))