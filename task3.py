
def PointCoordinate():
    point_x = input('введите точку X: ')
    point_y = input('введите точку Y: ')
    while not point_x.isdigit() and not point_y.isdigit():
        print("Одно или оба значения не подходят")
        point_x = input('введите точку X: ')
        point_y = input('введите точку Y: ')
    point_x = int(point_x)
    point_y = int(point_y)
    if point_x == 0 or point_y == 0:
        print('Ошибка')
    elif point_x > 0 and point_y > 0:
        print('Это первая четверть')
    elif point_x < 0 and point_y > 0:
        print('Это вторая четверть')
    elif point_x < 0 and point_y < 0:
        print('Это третья четверть')
    elif point_x > 0 and point_y < 0:
        print('Это четвертая четверть')
PointCoordinate()
