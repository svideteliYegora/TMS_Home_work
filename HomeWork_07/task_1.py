'''
Ввести предложение состоящее из двух слов. Поменять местами слова, добавить восклицательный знак в начало и конец,
слова разделить 3 символами (пробел, восклицательный знак и еще пробел), вывести итоговое предложение на экран.
Задание необходимо выполнить 3-мя разными способами форматирования.
'''

words = input('Enter sentence consisting of two words:\n').split()

# first method
print(f"!{words[1]} ! {words[0]}!")

# second method
print("!" + words[1] + ' ' + '!' + ' ' + words[0] + '!')

# third method
print("!{second_word} ! {first_word}!".format(second_word=words[1], first_word=words[0]))