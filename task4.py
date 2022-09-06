quarter = input('Введите номер четверти от 1 до 4: ')

def Coordinate(quarter):
    if quarter == 1:
        print(f"В четверти №{quarter}: Х (от 0 до +∞), Y (от 0 до +∞)")
    elif quarter == 2:
        print(f"В четверти №{quarter}: Х (от 0 до -∞), Y (от 0 до +∞)")
    elif quarter == 3:
        print(f"В четверти №{quarter}: Х (от 0 до -∞), Y (от 0 до -∞)")
    elif quarter == 4:
        print(f"В четверти №{quarter}: Х (от 0 до +∞), Y (от 0 до -∞)")
    else: print('Такой четверти нет.')
Coordinate(quarter)
if type(quarter) == int:
    if quarter < 5 and quarter > 0:
        Coordinate(quarter)
    else:
        print('Такой четверти не существует')
        quit
else:
    print('Данное значение не подходит!')
