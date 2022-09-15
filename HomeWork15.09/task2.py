# 2-Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# *Пример:*

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

def list_sum(list_number:list):
    '''
    Нахождние произведения пар чисел из списка, с созданием новго списка
    '''
    new_list = [list_number[i] * list_number[-(i+1)] for i in range(len(list_number) // 2)]
    if len(list_number) % 2 != 0:
        new_list.append(list_number[(len(list_number)//2)]**2)
    return print(new_list)

test_1 = [2, 3, 4, 5, 6]
test_2 = [2, 3, 5, 6]
list_sum(test_1)
list_sum(test_2)