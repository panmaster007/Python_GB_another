'''
    Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[N].
    Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
    В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
    Ввод: 5
    Ввод: 3 2 3 7 5
    Ввод: 3
    -> 2
'''

def number_of_numbers_in_the_list():
    numbers_in_list = int(input('Введите количество чисел в списке: '))
    some_list = list(map(int, input("Введите список: ").split()))

    if len(some_list) != numbers_in_list:
        return "Error"
    
    number = int(input('Введите число: '))

    counter = 0

    for i in some_list:
        if i == number:
            counter += 1

    return f"\n Список: {some_list}\n Число: {number}\n -> {counter}"


print(number_of_numbers_in_the_list())