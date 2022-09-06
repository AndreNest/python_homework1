point_x = input('введите точку X: ')
point_y = input('введите точку Y: ')

def PointCoordinate(point_x, point_y):
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

if type(point_x) == int and type(point_y) == int:
    PointCoordinate(point_x, point_y)
else:
    print('Данное значение не подходит!')
