from math import sqrt
def SearchSegment(point_x1, point_y1, point_x2, point_y2):
    print("Длина отрезка = ", round(sqrt((point_x1 - point_x2) ** 2 + (point_y1 - point_y2) ** 2), 2))
SearchSegment(float(input('Введите x1: ')), float(input('Введите y1: ')),
              float(input('Введите x2: ')), float(input('Введите y2: ')))
              
