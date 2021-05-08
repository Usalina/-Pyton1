def wage (arg_1, arg_2, arg_3):
    return ((salary * watch) + prize)

start=int(input('Хотите рассчитать заработную плату? (да - 1 / нет - 2): '))
while start != 2:
    if start == 1:
        name=input('Имя Фамилия сотрудника: ').title()
        salary=int(input('Введите стоимость часа работы: '))
        watch=int(input('Введите количество отработанных часов: '))
        prize=int(input('Введите сумму премии: '))
        print(f'Заработная плата', name, ':', (wage(salary, watch, prize)))
        start = int(input('Хотите поссчитать заработную плату? (да - 1 / нет - 2): '))
    else:
        print('Неверно')
        start = int(input('Хотите рассчитать заработную плату? (да - 1 / нет - 2): '))
print('До свидания')
