def my_func(name, surname, dob, city, email, fone):
    return print(f'{name} {surname}, {dob} года рождения, контакты: {email}{fone}')


name = input('Ваше имя: ')
surname = input('Ваше фамилия: ')
dob = input('Год рождения: ')
city = input('В каком городе Вы живете: ')
email = input('Ваш Email: ')
fone = input('Ваш телефон: ')

print(my_func(name, surname, dob, city, email, fone))