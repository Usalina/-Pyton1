
#Вариант 1 (простой)

list=[3, 7, 'Leo', 'Mary', 2.780, 0.5]

print(type(list[0]))
print(type(list[1]))
print(type(list[2]))
print(type(list[3]))
print(type(list[4]))
print(type(list[5]))

#Вариант 2

i=0
while len(list) != 0:
    print(type(list[i]))
    i+=1;
print('Конец')