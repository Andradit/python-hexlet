'''Напишите функцию get_unique(), которая принимает произвольное количество
списков и возвращает список, содержащий все элементы из всех списков, но без
повторений.'''


def get_unique(*args):
    result = set()
    for i in args:
        result = set(i) | result
    return list(result)

# SOLUTION
# def get_unique(*args):
#     result = set()
#     for data in args:
#         result |= set(data)
#     return [*result]


print(get_unique([1, 2, 3], [3, 4, 5], [5, 6, 7]))  # [1, 2, 3, 4, 5, 6, 7]
