my_list=str(input('введите несколько слов или цифр ')).split()

my_list1=[]

for el in my_list:
    my_list1.append(el[0:9])

for i in range(len(my_list1)):
    print(i+1, ')', my_list1[i])

