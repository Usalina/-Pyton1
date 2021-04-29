from itertools import count

new_list=[]

for el in count(2):
    new_list.append(el)
    if el > 7:
        break
print(new_list)

from itertools import cycle

count= 0
for el in cycle(new_list):
    new_list.append(el)
    if count > 9:
        break
    count +=1
print(new_list)

