"""Привычные нам структуры можно представить и как рекурсивные. Например,
у списка, есть голова (первый элемент) и хвост (последущие), у хвоста тоже
есть своя голова и хвост, который тоже можно разделить на голову и хвост. И
так далее до конца, где последний элемент списка можно представить как голова
плюс хвост из пустого списка. А вот уже пустой список невозможно разделить,
и наша рекурсия остановится."""

# [1, 2, 3] голова [1], хвост [2, 3]
# [2, 3] голова [2], хвост [3]
# [3] голова [3], хвост пустой список []
# [] # остановка
"""В этом упражнении вам нужно будет реализовать три несложные функции, 
но через рекурсивный процесс:

    - length() принимает список и возвращает его длину"""

# length([1, 2, 3])  # 3

"""
    - reverse_range() принимает два числа begin и end и возвращает перевернутый 
список всех чисел между. Для простоты договоримся, что begin <= end"""

# reverse_range(1, 1)  # [1]
# reverse_range(1, 3)  # [3, 2, 1]

"""
    - filter_positive() принимает список чисел и возвращает новый только с 
положительными элементами"""

# filter_positive([])  # []
# filter_positive([-3])  # []
# filter_positive([1, -2, 3])  # [1, 3]

"""Вы, конечно, можете реализовать функции привычным итеративным способом, 
но попробуйте сменить угол зрения."""


# def length(items):
#     print(f'{items=}')
#     head, *tail = items
#     print(f'{head=}, {tail=}')
#     if not tail:
#         print(1)
#         return 1
#     result = length(tail) + 1
#     print(result)
#     return result
#
#
# print(length([1, 2, 3, 6, 8]))  # 5


# def reverse_range(begin, end):
#     if begin <= end:
#         result = reverse_range(begin + 1, end)
#         result.append(begin)
#         return result
#     return []
#
#
# # print(list(range(end, begin-1, -1)))
#
#
# # reverse_range(1, 1)  # [1]
# print(reverse_range(1, 3))  # [3, 2, 1]

def filter_positive(items):
    *head, tail = items
    if not head:
        return []
    result = filter_positive(head)
    # print()
    if head[0] > 0:
        result.append(head[0])
    return result


# print(filter_positive([]))  # []
print(filter_positive([-3]))  # []
print(filter_positive([1, -2, 3]))  # [1, 3]

# """Вывести список с помощью рекурсии (поэлементно) на экран, не используя
# for, и вернуть количество элементов в списке"""
#
#
def element_show(item):
    if not item:
        return 0
    else:
        print(item[0])
        return 1 + element_show(item[1:])
#
#
print(element_show([1, 3, 4, 5, 6]))
# # 1
# # 3
# # 4
# # 5
# # 6
#
#
# def element_count(item):
#     if not item:
#         return 0
#     return 1 + element_count(item[1:])
# #
# #
# print(element_count([1, 3, 4, 5, 6, 8, 5]))  # 7


# def sum(n):
#     if n == 1:
#         return 1
#
#     return n + sum(n - 1)
#
# print(sum(100)) # <= 5050

# def collatz(n):
#     if n == 1:
#         return True
#     if n % 2 == 0:
#         return collatz(n // 2)
#     return collatz(n * 3 + 1)
#
#
# n = 3
# print(f'Collatz of {n}')
# collatz(n)
