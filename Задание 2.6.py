# вроде все работает, но что-то точно не правильно

new_name=str(input(('Название товара ')))
new_price=int(input('Цена товара '))
new_quantity=int(input('Количество '))
new_unit=str(input('Еденица измерения '))

my_list=[(1, {'name': 'компьютер', 'price': 20000, 'quantity': 5, 'unit':'шт'}),
(2, {'name': 'принтер', 'price': 6000, 'quantity': 3, 'unit':'шт'}),
(3, {'name': 'сканер', 'price': 2000, 'quantity': 1, 'unit':'шт'}),
(4, {'name': 'колонки', 'price': 5000, 'quantity': 2, 'unit':'шт'})]

new_diet={'name': new_name, 'price': new_price, 'quantity': new_quantity, 'unit':new_unit}

new_list=(int(len(my_list))+1, new_diet)

my_list.append(new_list)

list_name=[]
for dict in my_list:
    dicts=(dict[1])
    for key, el in dicts.items():
        result=(dicts['name'])
        list_name.append(str(result))
set(list_name)
print(f'{"name"}{set(list_name)}')

list_name=[]
for dict in my_list:
    dicts=(dict[1])
    for key, el in dicts.items():
        result=(dicts['price'])
        list_name.append(str(result))
set(list_name)
print(f'{"price"}{set(list_name)}')

list_name=[]
for dict in my_list:
    dicts=(dict[1])
    for key, el in dicts.items():
        result=(dicts['quantity'])
        list_name.append(str(result))
set(list_name)
print(f'{"quantity"}{set(list_name)}')

list_name=[]
for dict in my_list:
    dicts=(dict[1])
    for key, el in dicts.items():
        result=(dicts['unit'])
        list_name.append(str(result))
set(list_name)
print(f'{"unit"}{set(list_name)}')







