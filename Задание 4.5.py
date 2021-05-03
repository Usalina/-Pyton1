from functools import reduce

my_list=([x for x in range(101, 1001) if x%2==0])

def my_multip(first, second):
    return first * second

result = reduce (my_multip, my_list)
print(result)