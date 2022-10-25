'''
Документ article.txt содержит следующий текст:

Вечерело
Жужжали мухи
Светил фонарик
Кипела вода в чайнике
Венера зажглась на небе
Деревья шумели
Тучи разошлись
Листва зеленела

Требуется реализовать функцию longest_words(file), которая выводит слово, имеющее максимальную длину
(или список слов, если таковых несколько).

'''

def longest_words(file):
    long_word = ''
    all_words = []
    longest_words_list = []

    with open(file, encoding="utf-8") as read_file:
        for line in read_file.read().split():
            all_words.append(line)
            if len(line) > len(long_word):
                long_word = line

        for word in all_words:
            if len(word) == len(long_word):
                longest_words_list.append(word)

    if len(longest_words_list) > 1:
        print(longest_words_list)
    else:
        print(long_word)

longest_words('article.txt')


