data=input('Введите числа через пробел, если хотите закончить - введите X (анг): ')
ind_x=(data.find('X'))

list2=[]
while ind_x==-1:
    list1 = data.split()
    list3 = list(map(int, list1))
    for el in list3:
        list2.append(el)
    print(sum(list2))
    data = input('Введите числа через пробел, если хотите закончить - введите X (анг): ')
    ind_x = (data.find('X'))
    list1 = data.split()
index = int(len(list1))
del list1[index-1]
list4 = list(map(int, list1))
for el in list4:
    list2.append(el)
print(sum(list2))
print('Конец')