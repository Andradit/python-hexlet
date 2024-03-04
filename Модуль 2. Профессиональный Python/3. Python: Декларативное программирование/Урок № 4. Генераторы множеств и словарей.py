"""Вам необходимо реализовать функцию number_of_unique_letters(). Эта функция
должна подсчитывать количество уникальных букв в строке-аргументе без учёта
регистра:"""

# number_of_unique_letters("")  # 0
# number_of_unique_letters("abc")  # 3
# number_of_unique_letters("A-a-a-a-a-a!")  # 1
# number_of_unique_letters("\\(O_o)/")  # 1
# number_of_unique_letters("AaBbCcDd")  # 4

"""Подсказки
Вам может пригодиться что-то из этого:"""

'Hello World!'.lower()  # 'hello world!'
'o_O'.upper()  # 'O_O'
'z'.isalpha()  # True
'_'.isalpha()  # False


def number_of_unique_letters(text):
    return len([symbol for symbol in set(text.lower()) if symbol.isalpha()])


'ALTERNATIVE'
# def number_of_unique_letters(text):
#     counter = 0
#     for symbol in set(text.lower()):
#         if symbol.isalpha():
#             counter += 1
#     return counter


'SOLUTION'

# def number_of_unique_letters(text):
#     return len({char.lower() for char in text if char.isalpha()})

print(number_of_unique_letters(""))  # 0
print(number_of_unique_letters("abc"))  # 3
print(number_of_unique_letters("A-a-a-a-a-a!"))  # 1
print(number_of_unique_letters("\\(O_o)/"))  # 1
print(number_of_unique_letters("AaBbCcDd"))  # 4
