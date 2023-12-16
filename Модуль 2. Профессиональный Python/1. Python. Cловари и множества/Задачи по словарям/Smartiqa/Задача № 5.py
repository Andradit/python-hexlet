# from collections import Counter
# from functools import reduce
'''Имеется ряд словарей с пересекающимися ключами (значения - положительные
числа). Напишите 2 функции, которые делают с массивом словарей следующие
операции:

1-ая функция max_dict(*dicts) формирует новый словарь по правилу:
Если в исходных словарях есть повторяющиеся ключи, выбираем среди их значений
максимальное и присваиваем этому ключу (например, в словаре_1 есть ключ "а" со
значением 5, и в словаре_2 есть ключ "а", но со значением 9. Выбираем
максимальное значение, т. е. 9, и присваиваем ключу "а" в уже новом словаре).

Если ключ не повторяется, то он просто переносится со своим значением в новый
словарь (например, ключ "с" встретился только у одного словаря, а у других его
нет. Следовательно, переносим в новый словарь этот ключ вместе с его
значением).Сформированный словарь возвращаем.

2-ая функция sum_dict(*dicts) суммирует значения повторяющихся ключей. Значения
остальных ключей остаются исходными. (Проводятся операции по аналогу первой
функции, но берутся не максимумы, а суммы значений одноименных ключей).
Функция возвращает сформированный словарь.'''


dict_1 = {'a': 12, 'b': 33, 'c': 10, 'd': 10, 'e': 2, 'f': 90}
dict_2 = {'a': 12, 'b': 7, 'c': 1, 'd': 2, 'e': 112}
dict_3 = {'a': 3, 'b': 3, 'c': 60, 'd': 8, 'e': 725, 'f': 111}
dict_4 = {'a': 1, 'b': 13, 'c': 31, 'd': 9, 'e': 556}


def max_dict(*args):
    res_dict = {}
    for dicts in args:
        for key, value in dicts.items():
            if key not in res_dict:
                res_dict[key] = value
            elif value > res_dict[key]:
                res_dict[key] = value
    return res_dict


# SOLUTION
# def max_dict(*dicts):
#     return dict(reduce(lambda a, b: Counter(a) | Counter(b), dicts))

print(max_dict(dict_1, dict_2, dict_3, dict_4))
# {'a': 12, 'b': 33, 'c': 60, 'd': 10, 'e': 725, 'f': 111}


def sum_dict(*args):
    res_dict = {}
    for dicts in args:
        for key, value in dicts.items():
            if key not in res_dict:
                res_dict[key] = value
            else:
                res_dict[key] += value
    return res_dict

# SOLUTION
# def sum_dict(*dicts):
#     return dict(reduce(lambda a, b: Counter(a) + Counter(b), dicts))


print(sum_dict(dict_1, dict_4, dict_3))
# {'a': 16, 'b': 49, 'c': 101, 'd': 27, 'e': 1283, 'f': 201}
print(sum_dict(dict_1, dict_2, dict_3, dict_4))
# {'a': 28, 'b': 56, 'c': 102, 'd': 29, 'e': 1395, 'f': 201}
