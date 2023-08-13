"""Цель упражнения — функция count_all(). Эта функция должна принимать на вход
итерируемый источник и возвращать словарь. Ключами этого словаря должны стать
элементы источника, при этом значения должны отражать количество повторов
элемента в коллекции-источнике.

Посмотрим на этих примерах, как должна работать эта функция:

count_all(["cat", "dog", "cat"])  # {"cat": 2, "dog": 1}
count_all("hello")  # {'h': 1, 'e': 1, 'l': 2, 'o': 1}
count_all("*" * 20)  # {'*': 20}"""


def count_all(elements):
    dict = {}

    for element in elements:
        # print(element)
        # dict[element] = 0
        if element in dict:
            dict[element] = dict[element] + 1
            # print(dict)
        else:
            dict[element] = 1
            # print(dict)
    return dict


print(count_all(["cat", "dog", "cat"]))
print(count_all("hello"))
print(count_all("*" * 20))


"""def count_all(items):  ---> solution
    counters = {}
    for item in items:
        counters[item] = counters.get(item, 0) + 1
    return counters"""
