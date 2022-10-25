'''
Сделать функцию которая на вход принимает строку. Анализирует ее исключительно методом isdigit() без доп. библиотек
и переводит строку в число. Функция умеет распознавать отрицательные числа и десятичные дроби.
'''

def converting_string_to_number(string: str) -> None:
    try:
        if string.isdigit() == True:
            print(f"You enter positive integer number: {int(string)}")
        elif string[0] == '-' and string[1:].isdigit() == True:
            print(f"You enter negative integer number: {int(string)}")
        elif string[0] == '-':
            print(f"You enter negative float number: {float(string)}")
        else:
            print(f"You enter positive float number: {float(string)}")

    except ValueError:
        print(f"You enter not correct number: {string}")

converting_string_to_number(input('Enter number:\n'))
