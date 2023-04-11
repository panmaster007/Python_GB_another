'''
    Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
    Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. 
    Выведите минимальное количество монет, которые нужно перевернуть
'''


def coin(number_of_coins):
    obverse = 0     #решка
    reverse = 0     #орел

    while number_of_coins > 0:
        side_of_the_coin = input("Выберите сторону монеты (1 - решка; 0 - орел): ")
        if side_of_the_coin not in ('0', '1'):
            raise TypeError
        if side_of_the_coin == '1':
            obverse += 1
        else:
            reverse += 1
        number_of_coins -= 1

    if obverse < reverse:
        return f"Минимальное количество монет, которые нужно перевернуть : {obverse}"
    else:
        return f"Минимальное количество монет, которые нужно перевернуть : {reverse}"
    

print(coin(5))