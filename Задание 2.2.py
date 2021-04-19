my_list=str(input('Введите данные через пробел ')).split()



i = int((len(my_list)) // 2)
if int(len(my_list))%2==1:
    last_data=my_list[-1]
    del my_list[-1]
    print(my_list)
    while i!=0:
        last_data1 = my_list[i * 2 - 1]
        del my_list[i*2-1]
        my_list.insert((i*2)-2, last_data1)
        i -= 1
    my_list.append(last_data)
    print(my_list)

elif int(len(my_list))%2==0:
    while i != 0:
        last_data2 = my_list[i*2-1]
        del my_list[int(i*2-1)]
        my_list.insert(int((i * 2) - 2), last_data2)
        i -= 1
    print(my_list)