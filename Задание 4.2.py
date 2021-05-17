list_1=[int(i) for i in input('Введите числа через пробел: ').split()]

list_2=[]


for i in range(1, len(list_1)):
    if list_1[i] > list_1[i - 1]:
        el = list_1[i]
        list_2.append(el)
print(list_2)