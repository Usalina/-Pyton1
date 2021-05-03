
f=open('file_5.txt', 'w')

new_str = input('Введите числа через пробел: ')
f.write(new_str)
f.close()

new_list=list(map(int, new_str.split()))
print(sum(new_list))