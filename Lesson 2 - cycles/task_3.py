'''
    Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
'''

def degrees_of_two(number):
    start_num = 1
    while start_num <= number:
        print(start_num, end=' ')
        start_num *= 2

degrees_of_two(50)