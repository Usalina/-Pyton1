
my_list=[8, 6, 9, 1, 2, 2, 2, 3, 0, 5]

new_list=[el for el in my_list if my_list.count(el) == 1]

print(new_list)