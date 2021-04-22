month=str(input('Введите порядковый номер месяца  '))

list_winter=['1', '2', '12']
list_spring=['3', '4', '5']
list_summer=['6', '7', '8']
list_autumn=['9', '10', '11']

if (month in list_winter) == True:
    print('Зима')
elif (month in list_spring) == True:
    print('Весна')
elif (month in list_summer) == True:
    print('Лето')
elif (month in list_autumn) == True:
    print('Осень')


dict={'1': 'Зима', '2': 'Зима', '12': 'Зима', '3': 'Весна', '4': 'Весна', '5': 'Весна', '6': 'Лето', '7': 'Лето', '8':'Лето', '9':'Осень', '10':'Осень', '11':'Осень'}

print(dict[month])



