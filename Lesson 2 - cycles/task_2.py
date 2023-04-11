'''
    Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. 
    Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки. 
    Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.
'''

from termcolor import cprint
from art import tprint


def guess_the_number():
    tprint("Let's play")
    cprint("Загадайте два два натуральных числа X и Y (X,Y≤1000))\n", 'green')

    sum_of_numbers = int(input("Введите сумму чисел: "))
    product_of_numbers = int(input("Введите произведение чисел: "))

    first_number = int((sum_of_numbers + ((-sum_of_numbers) ** 2 - 4 * product_of_numbers) ** 0.5) / 2)
    second_number = int((sum_of_numbers - ((-sum_of_numbers) ** 2 - 4 * product_of_numbers) ** 0.5) / 2)

    return f"Ответ: {first_number} и {second_number}"

print(guess_the_number())