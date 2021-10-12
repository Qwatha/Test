"""
    Написать метод/функцию, который/которая на вход принимает число (int),
    а на выходе выдает слово “компьютер” в падеже, соответствующем указанному количеству.
    Например, «25 компьютеров», «41 компьютер», «1048 компьютеров».
"""


def func(number):
    if type(number) != int:
        return "Введите челое число"
    if number % 100 == 11:
        string = f'{number} компьютеров'
    elif number % 10 == 1:
        string = f'{number} компьютер'
    elif (number % 10 == 2 and number % 100 != 12) or (number % 10 == 3 and number % 100 != 13) or (
            number % 10 == 4 and number % 100 != 14):
        string = f'{number} компьютера'
    else:
        string = f'{number} компьютеров'
    return string

# Время 15-20 минут
