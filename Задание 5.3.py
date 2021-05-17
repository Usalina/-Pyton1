
f=open('file_3.txt', 'r')
new_dict={}
list_salary=[]
count=0
for line in f:
    new_line=(line.split())
    list_salary.append(int(new_line[1]))
    count+=1
    for el in new_line:
        new_dict[new_line[0]]=new_line[1]

list_min=[]
for key, val in new_dict.items():
    if int(val) < 20000:
        list_min.append(key)

print(f'Доход менее 20000: ', list_min)

print(f'средний доход равен: ', sum(list_salary)/count)



f.close()