def my_func(arg1, arg2):
    return arg1+arg2

numbers=[]
for i in range(3):
    number=int(input('Введите число: '))
    numbers.append(number)

list.sort(numbers)
del numbers[0]

arg1=int(numbers[0])
arg2=int(numbers[1])

print(my_func(arg1, arg2))

