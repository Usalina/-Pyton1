number=int(input('Введите время в секундах: '))

hour=int(number//3600)
min=int(number%3600//60)
sec=int(number%60)

print(f"{hour:02}:{min:02}:{sec:02}")
