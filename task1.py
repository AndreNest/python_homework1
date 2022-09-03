day = int(input('Введите число от 1 до 7: '))
if day > 5 and day < 8:
    print(f'{day} - это выходной')
elif day > 0 and day < 6:
    print(f'{day} - это будний день')
else: print('Не правильное значение')
