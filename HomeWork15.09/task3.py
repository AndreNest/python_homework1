# 3-Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и
# минимальным значением дробной части элементов.
# *Пример:*

# - [1.1, 1.2, 3.1, 5.17, 10.02] => 0.18 или 18
#  - [4.07, 5.1, 8.2444, 6.98] - 0.91 или 91

def max_min_dif(list_float_numbers: list):
    count = 0
    while count < len(list_float_numbers):
        list_float_numbers[count] = round(
            list_float_numbers[count] - (int(list_float_numbers[count])), 10)
        count += 1
    diff_number = round((max(list_float_numbers)-min(list_float_numbers)), 10)
    print(f'{diff_number} или {int(diff_number* 100)}')

test_1 = [1.1, 1.2, 3.1, 5.17, 10.02]
test_2 = [4.07, 5.1, 8.2444, 6.98]
max_min_dif(test_1)
max_min_dif(test_2)
