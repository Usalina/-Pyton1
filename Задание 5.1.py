
f=open('new_file.txt', 'w')

str=input('Введите данные: ')
f.write(str)
f.write('\n')
while len(str) >= 1:
    str = input('Введите данные: ')
    f.write(str)
    f.write('\n')
    if len(str) == 0:
        break
f.close()
