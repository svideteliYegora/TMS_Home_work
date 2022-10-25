'''
Создать функцию <fib(n)>, генерирующую <n> чисел Фибоначчи с минимальными затратами ресурсов.
'''

def fib(n: int) -> int:
    first_number = 0
    second_number = 1
    sum_numbers = 0
    if n > 1:
        yield first_number
        yield second_number
    while n:
        sum_numbers = first_number + second_number
        if sum_numbers > n:
            break
        yield sum_numbers
        first_number = second_number
        second_number = sum_numbers

generator_fib = fib(5000)

for i in generator_fib:
    print(i)

