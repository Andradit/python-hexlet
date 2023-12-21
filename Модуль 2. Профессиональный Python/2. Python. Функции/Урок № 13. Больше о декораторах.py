from collections import OrderedDict
from functools import wraps

"""В этот раз вы снова будете реализовывать мемоизирующий декоратор
"memoizing". Но на этот раз декоратор должен принимать аргумент, задающий
максимальное количество запоминаемых значений. При превышении количества
запомненных значений лишние должны быть отброшены, причём сначала — самые
старые!

Напоминаю, мемоизируемые функции считать численными функциями одного
аргумента. И не забудьте про functools.wraps!"""

# @memoizing(3)
# def f(x):
#     print('Calculating...')
#     return x * 10


# f(1)  # => Calculating...
# # 10
# f(1)  # будет "вспомнено"
# # 10
# f(2)  # => Calculating...
# # 20
# f(3)  # => Calculating...
# # 30
# f(4)  # вытеснит запомненный результат для "1"
# # => Calculating...
# # 40
# f(1)  # будет перевычислено
# # => Calculating...
# # 10

"""Хоть в современном Python словарь и помнит, в каком порядке добавлялись 
ключи, но я не рекомендую строить логику, опираясь на это свойство. 
Используйте вспомогательную структуру для хранения порядка ключей."""


def memoizing(max_count):
    def wrapper(func):
        res_dict = {}
        ordered_dict = OrderedDict(res_dict)

        @wraps(func)
        def inner(arg):
            print(ordered_dict)
            if arg in ordered_dict:
                return ordered_dict[arg]
            result = func(arg)
            ordered_dict[arg] = result
            if len(ordered_dict) > max_count:
                first_element = list(ordered_dict.items())[0]
                ordered_dict.move_to_end(key=first_element[0])
                ordered_dict.popitem()
            return result

        return inner

    return wrapper


'SOLUTION'
# from functools import wraps


# def memoizing(limit):
#     """
#     Make decorator that will remember recent results of function (up to
#     limit).
#
#     Arguments:
#         limit, maximum number of results to remember
#
#     Returns:
#         memoizing decorator
#
#     """
#
#     def wrapper(function):
#         """
#         Memoize function.
#
#         Arguments:
#             function, it will be memoized
#
#         Returns:
#             memoized version of function
#
#         """
#         memory = {}
#         order = []
#
#         @wraps(function)
#         def inner(argument):
#             memoized_result = memory.get(argument)
#             if memoized_result is None:
#                 memoized_result = function(argument)
#                 memory[argument] = memoized_result
#                 order.append(argument)
#                 if len(order) > limit:
#                     oldest_argument = order.pop(0)
#                     memory.pop(oldest_argument)
#             return memoized_result
#
#         return inner
#
#     return wrapper


@memoizing(3)
def f(x):
    print('Calculating...')
    return x * 10


print(f(1))  # => Calculating...
# 10
print(f(1))  # будет "вспомнено"
# 10
print(f(2))  # => Calculating...
# 20
print(f(3))  # => Calculating...
# 30
print(f(4))  # вытеснит запомненный результат для "1"
# => Calculating...
# 40
print(f(1))  # будет перевычислено
# => Calculating...
# 10
print(f(5))  # будет перевычислено
# => Calculating...
# 10
