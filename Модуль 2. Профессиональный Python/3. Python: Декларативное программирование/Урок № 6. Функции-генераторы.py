"""Вам предстоит потренироваться в написании генераторных функций и написать:

    - функцию my_map(f, xs), которая должна работать как упрощенная версия map()
    - функцию my_filter(f, xs) — упрощенный вариант filter()
    - функцию replicate_each(n, xs) должен выдавать на выход по n копий для
    каждого элемента итератора xs

Функции должны работать так:"""


# list(my_map(abs, [-1, 2, -3]))  # [1, 2, 3]
# list(my_filter(lambda x: x % 2 == 1, range(10)))  # [1, 3, 5, 7, 9]
# list(replicate_each(1, [1, 'a']))  # [1, 'a']
# list(replicate_each(3, [1, 'a']))  # [1, 1, 1, 'a', 'a', 'a']
# list(replicate_each(0, [1, 'a']))  # []

def my_map(function, source):
    for elem in source:
        yield function(elem)


def my_filter(condition, source):
    for elem in source:
        if condition(elem):
            yield elem


def replicate_each(replicate_count, source):
    for elem in source:
        for _ in range(replicate_count):
            yield elem


'SOLUTION'


# def my_map(function, source):
#     for arg in source:
#         yield function(arg)
#
#
# def my_filter(condition, source):
#     for arg in source:
#         if condition(arg):
#             yield arg
#
#
# def replicate_each(number, source):
#     for value in source:
#         yield from (value for _ in range(number))

"""     yield from i, это сокращенная форма для
        for x in i:
             yield x"""

print(list(my_map(abs, [-1, 2, -3])))  # [1, 2, 3]
print(list(my_filter(lambda x: x % 2 == 1, range(10))))  # [1, 3, 5, 7, 9])
print(list(replicate_each(1, [1, 'a'])))  # [1, 'a']
print(list(replicate_each(3, [1, 'a'])))  # [1, 1, 1, 'a', 'a', 'a']
print(list(replicate_each(0, [1, 'a'])))  # []
