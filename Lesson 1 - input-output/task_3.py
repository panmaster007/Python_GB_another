'''
    Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. 
    Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. 
    Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.

    *Пример:*

    385916 -> yes
    123456 -> no

'''


def lucky_ticket(number):
    if not isinstance(number,int) or len(str(number)) != 6:
        return 'Error'
    
    from_int_to_str = str(number)

    sum1 = 0
    sum2 = 0

    for i in from_int_to_str[:3]:
        sum1 += int(i)

    for i in  from_int_to_str[3:]:
        sum2 += int(i)

    if sum1 == sum2:
        return f"{number} -> yes"
    else:
        return f"{number} -> no"
    

print(lucky_ticket(385916))