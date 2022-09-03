
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
PointCoordinate(point_x = int(input('введите точку X: ')), point_y = int(input('введите точку Y: ')))