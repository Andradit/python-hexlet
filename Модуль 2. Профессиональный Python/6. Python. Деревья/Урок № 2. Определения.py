"""В этом задании под деревом понимается любой список элементов, которые в
свою очередь могут быть также деревьями или списками. Например:"""
from typing import List

# [
# 3, # Лист
# [5, 3], # Узел
# [[2]]  # Узел
# ]

"""Больше примеров можно найти в тестах.

Реализуйте функцию remove_first_level(). Она должна принимать на вход дерево 
и возвращать новое дерево, элементами которого являются потомки вложенных 
узлов:"""

# from solution import remove_first_level
#
# tree1 = [[5], 1, [3, 4]]
# remove_first_level(tree1)  # [5, 3, 4]
# tree2 = [1, 2, [3, 5], [[4, 3], 2]]
# remove_first_level(tree2)  # [3, 5, [4, 3], 2]

"""Подсказки
Подключенный в модуле пакет itertools можно использовать, 
но это необязательно"""
from itertools import chain


def remove_first_level(tree):
    res = []
    for i in tree:
        if isinstance(i, list):
            for x in i:
                res.append(x)
                # a = list(chain(x))
    return res


tree1 = [[5], 1, [3, 4]]
print(remove_first_level(tree1))  # [5, 3, 4]
tree2 = [1, 2, [3, 5], [[4, 3], 2]]
print(remove_first_level(tree2))  # [3, 5, [4, 3], 2]
