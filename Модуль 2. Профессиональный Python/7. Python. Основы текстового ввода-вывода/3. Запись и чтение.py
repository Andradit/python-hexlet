# import re
"""Реализуйте функцию count_words(), которая принимает на вход путь до
текстового файла, и возвращает словарь частот встречающихся слов. При подсчете
слов не учитывайте регистр."""

# The Python language was not named after a long snake, but after the British
# comedy show Monty Python Flying Circus


# count_words('python.txt')

# {
#  'the': 2,
#  'python': 2,
#  'after': 2,
#  'language': 1,
#  'was': 1,
#  'not': 1,
#  'named': 1,
#  'a': 1,
#  'long': 1,
#  'snake': 1,
#  'but': 1,
#  'british': 1,
#  'comedy': 1,
#  'show': 1,
#  'monty': 1,
#  'flying': 1,
#  'circus': 1
# }

'''Подсказки
Для разбивки текста на слова можно использовать метод split(), но учтите что
какие-то слова могут оканчиваться на знаки препинания.'''

file = open('Модуль 2. Профессиональный Python/7. Python. Основы текстового'
            'ввода-вывода/foo.txt', 'w')
file.write("The Python language was not named after a long snake, but "
           "after the British comedy. show Monty Python Flying Circus")
file.close()


def count_words(path):
    text = open(path).read()
    text = text.lower()
    punctuation = [',', '.', '?', '!', ':']
    for i in punctuation:
        text = text.replace(i, '')
    result = text.split(' ')
    # result = (re.split("[ ,.]", text))
    res_dict = {}
    for i in result:
        # if i != ',' and i != '':
        res_dict[i] = result.count(i)
    return res_dict


# SOLUTION
# from collections import Counter


# def count_words(filepath):
#     data = open(filepath).read()
#     punctuation = [',', '.', '?', '!', ':']
#     words = []
#     for word in data.split():
#         word = word.lower()
#         for p in punctuation:
#             if word.endswith(p):
#                 word = word[:-1]
#         words.append(word)
#     return Counter(words)


print(count_words('foo.txt'))
