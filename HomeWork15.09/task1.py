# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
#*Пример:*
#- [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

def sum_foud_element(list_number:list):
    '''
    Сложение нечетных элементов из списка
    '''
    sum_numb = 0
    for i in range(len(list_mumber)):
        if i % 2 != 0:
            sum_numb += list_mumber[i]
    return print(sum_numb)
list_mumber = [2, 3, 5, 9, 3]
sum_foud_element(list_mumber)
