def day():
    num = input('Введите число: ')
    while num.isdigit() is not True:
        print('Не правильное значение')
        num = input('Введите число: ')
    num = int(num)
    if 0 < num < 6:
        print("Это будний день")
    elif 5 < num < 8:
        print("Это выходной")
    else:
        print("такого дня не существует")

day()
