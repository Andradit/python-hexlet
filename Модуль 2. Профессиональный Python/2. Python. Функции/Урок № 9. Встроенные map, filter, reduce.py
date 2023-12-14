import operator
from functools import reduce

'''В этом упражнении вам предстоит попрактиковаться в использовании встроенных
функций map(), filter(), reduce() (эту нужно импортировать из functools). На
их основе вам нужно реализовать три функции: keep_truthful(), abs_sum() и
walk().

Функция keep_truthful() должна принимать на вход итерируемый источник значений
и возвращать итератор, отдающий только те значения из источника, которые
"истинны" (вам пригодится функция operator.truth).'''

# list(keep_truthful([True, False, "", "foo"]))  # [True, 'foo']

'''Функция abs_sum() принимает на вход итерируемый источник чисел. Вернуть же
функция должна сумму абсолютных значений этих чисел (используйте sum и abs).'''

# abs_sum([-3, 7])  # 10
# abs_sum([])  # 0
# abs_sum([42])  # 42

'''walk() должна для некоего словаря с глубокой вложенностью уметь доставать
значение по указанному в виде iterable строк пути. В решении можете
использовать функцию operator.getitem.

Имейте в виду: мы считаем, что значения по указанному пути всегда доступны и
сама структура словаря всегда правильная. Это означает, что заранее
обрабатывать ошибки не нужно. Так что реализуйте "оптимистичное решение".'''

# walk({'a': {7: {'b': 42}}}, ["a", 7, "b"])  # 42
# walk({'a': {7: {'b': 42}}}, ["a", 7])  # {'b': 42}


def keep_truthful(iter_source):
    return filter(operator.truth, iter_source)


print(list(keep_truthful([True, False, "", "foo"])))  # [True, 'foo']


def abs_sum(iter_source):
    return sum(map(abs, iter_source))


print(abs_sum([-3, 7]))  # 10
print(abs_sum([]))  # 0
print(abs_sum([-42]))  # 42


def walk(dictionary, path):
    def inner(x, y):
        # print(f'{x=},{y=}')
        return dict.get(x, y)
    return reduce(inner, path, dictionary)
    # return reduce(dict.get, path, dictionary)


print(walk({'a': {7: {'b': 42}}}, ["a", 7, "b"]))  # 42
print(walk({'a': {7: {'b': 42}}}, ["a", 7]))  # {'b': 42}

# a = [1, 2, 3]
# b = ['a', 'b', 'c']

# a = {'a': {7: {'b': 42}}}
# b = operator.getitem(a, 'a')
# c = operator.getitem(b, 7)
# print(lambda x: operator.getitem(a, x))
# print(operator.getitem(a, 'a'))
# print(operator.getitem(b, 7))
# print(operator.getitem(c, 'b'))
# # print(operator.getitem(({'a': {7: {'b': 42}}}, ["a", 7])))


# SOLUTION
# from functools import reduce
# from operator import getitem, truth


# def keep_truthful(items):
#     return filter(truth, items)


# def abs_sum(numbers):
#     return sum(map(abs, numbers))


# def walk(dictionary, path):
#     return reduce(getitem, path, dictionary)
