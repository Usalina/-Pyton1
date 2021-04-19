earnings=int(input('Введите сумму выручки '))

cost=int(input('Введите сумму издержек '))

profit=earnings >cost

if earnings >cost:
    print('Финансовый результат - прибыль равна', earnings-cost, 'рублей')
    print('Рентабельность 1 к', earnings//cost, 'процентов')
    if profit>0:
        staff = int(input('Количество сотрудников '))
        print('Прибыль ', (earnings - cost) // staff, ' в расчете на одного сотрудника')
elif earnings <cost:
    print('Финансовый результат - убыток равен', cost-earnings, 'рублей')


