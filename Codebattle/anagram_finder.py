# from collections import defaultdict

"""Найти все анаграммы в массиве слов. Функция должна возвращать массив с 
массивами, где каждый внутренний массив - это набор слов, которые являются 
анаграммой друг к другу. Слова без анаграмм не должны попадать в результат. 
Если анаграмм во входящем массиве нет - возвращается подмассив со строкой 
"anagrams not found!". Порядок элементов важен, элементы сортируются в 
алфавитном порядке. 
"""


def solution(words: list[str]) -> list[list[str]]:
    dictionary = {}
    for word in words:
        symbol_set = ''.join(sorted(word))
        if symbol_set not in dictionary:
            dictionary[symbol_set] = [word]
        else:
            dictionary[symbol_set].append(word)

    for key, value in dictionary.items():
        if len(value) <= 1:
            dictionary[key] = ['anagrams not found!']
    return list(dictionary.values())


'ALTERNATIVE SOLUTION'

# def solution(words: List[str]) -> List[List[str]]:
#     temp = defaultdict(list)
#     for elem in words:
#         temp[str(sorted(elem))].append(elem)
#     for key, value in temp.items():
#         if len(value) <= 1:
#             temp[key] = ['anagrams not found!']
#     return list(temp.values())


print(solution(['mite', 'lake', 'item', 'kale', 'klae', 'this']))
