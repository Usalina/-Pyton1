
# Я совсем не поняла задание №7

from functools import reduce
from itertools import count

n=6

def fact(arg1):
    new_list=[]
    for el in count(1):
        new_list.append(el)
        if el == arg1:
            break
    return new_list

def my_multip(first, second):
    return first * second

result = reduce (my_multip, fact(n))
print(result)
