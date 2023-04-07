'''
    Задача 2: Найдите сумму цифр трехзначного числа.

    *Пример:*

    123 -> 6 (1 + 2 + 3)
    100 -> 1 (1 + 0 + 0) 

'''


def sum_of_digit(number : int):
    if not isinstance(number, int) or len(str(number)) != 3:
        raise TypeError
    
    digit1 = number // 100
    digit2 = (number % 100) // 10
    digit3 = number % 10

    return f"{number} -> {digit1+digit2+digit3} ({digit1} + {digit2} + {digit3})"


print(sum_of_digit(123))