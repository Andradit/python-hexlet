'''Цель упражнения — написать функцию collect_indexes(). Эта функция должна:

- принимать на вход коллекцию — некий итератор или итерируемый элемент
- возвращать словарь или подобную ему коллекцию. Ключом будет элемент
коллекции, а значением для ключа — список индексов коллекции, по которым
встречается этот элемент

d = collect_indexes("hello")
d["h"]  # [0]
d["e"]  # [1]
d["l"]  # [2, 3]
'''


def collect_indexes(elements):
    dict = {}

    for index, value in enumerate(elements):
        dict.setdefault(value, []).append(index)

    return dict


'''BEGIN
from collections import defaultdict  # ---> solution


def collect_indexes(items):
    result = defaultdict(list)
    for index, item in enumerate(items):
        result[item].append(index)
    return result
END'''


# from collections import defaultdict  ---> alternative solution (1)


# def collect_indexes(elements):
#     dict = defaultdict(list)

#     for value, key in enumerate(elements):
#         dict[key].append(value)

#     return dict


# def collect_indexes(elements):  ---> alternative solution (2)
#     dict = {}
#     for value, key in enumerate(elements):
#         dict[key] = dict.get(key, []) + [value]
#     # print(dict)
#     return dict


d = collect_indexes("hello")
print(d["h"])  # [0]
print(d["e"])  # [1]
print(d["l"])  # [2, 3]
