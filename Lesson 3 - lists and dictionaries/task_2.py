'''
    Задача 18: Требуется найти в массиве A[N] самый близкий по величине элемент к заданному числу X.
    Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
    В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
    Ввод: 5
    Ввод: 1 2 6 4 9
    Ввод: 8
    -> 9
'''

def elements_of_the_number():
    numbers_in_list = int(input('Введите количество чисел в списке: '))
    some_list = list(map(int, input("Введите список: ").split()))

    if len(some_list) != numbers_in_list:
        return "Error"
    
    number = int(input('Введите число: '))

    result = some_list[0]
    
    for i in some_list:
        if abs(number - result) > abs(number - i):
            result = i

    return f"\n Список: {some_list}\n Число: {number}\n -> {result}"

print(elements_of_the_number())