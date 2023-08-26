"""Реализуйте функцию merged(), которая объединяет несколько словарей в один
общий словарь. Функция принимает список словарей и возвращает результат в виде
словаря, в котором каждый ключ содержит множество (set) уникальных значений."""

# from solution import merged
# merged([{}, {}]) == {}
# True
# merged([
#     {'a': 1, 'b': 2},
#     {'b': 10, 'c': 100},
# ]) == {'a': {1}, 'b': {2, 10}, 'c': {100}}
# True
"""Подсказки
Функция может вернуть любой объект, подобный словарю. Вы можете выбрать
наиболее подходящий среди имеющихся в стандартной библиотеке."""


def merged(item_of_dict):
    dict = {}

    for element in item_of_dict:
        keys = element.keys()
        for k in keys:
            if k not in dict:
                dict[k] = {element[k]}
            else:
                dict[k].add(element[k])

    return dict


# from collections import defaultdict  --->solution


# def merged(dicts):
#     aggregate = defaultdict(set)
#     for source in dicts:
#         for key, value in source.items():
#             aggregate[key].add(value)
#     return aggregate

print(merged([
    {'a': 1, 'b': 2},
    {'b': 10, 'c': 100},
]))
