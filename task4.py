

def Coordinate():
    quarter = input('Введите номер четверти от 1 до 4: ')
    while not quarter.isdigit():
        print('Это не число')
        quarter = input('Введите номер четверти от 1 до 4: ')
    quarter = int(quarter)
    if quarter == 1:
        print(f"В четверти №{quarter}: Х (от 0 до +∞), Y (от 0 до +∞)")
    elif quarter == 2:
        print(f"В четверти №{quarter}: Х (от 0 до -∞), Y (от 0 до +∞)")
    elif quarter == 3:
        print(f"В четверти №{quarter}: Х (от 0 до -∞), Y (от 0 до -∞)")
    elif quarter == 4:
        print(f"В четверти №{quarter}: Х (от 0 до +∞), Y (от 0 до -∞)")
    else: print('Такой четверти нет.')
Coordinate()
