"""Привычные нам структуры можно представить и как рекурсивные. Например,
у списка, есть голова (первый элемент) и хвост (последущие), у хвоста тоже
есть своя голова и хвост, который тоже можно разделить на голову и хвост. И
так далее до конца, где последний элемент списка можно представить как голова
плюс хвост из пустого списка. А вот уже пустой список невозможно разделить,
и наша рекурсия остановится."""

# [1, 2, 3]  # голова [1], хвост [2, 3]
# [2, 3]  # голова [2], хвост [3]
# [3]  # голова [3], хвост пустой список []
# []  # остановка
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


def length(items):
    head, *tail = items
    if not tail:
        return head
    return length(tail)


print(length([1, 2, 3, 6]))  # 3


def reverse_range(begin, end):
    item = []
    if begin <= end:
        for x in range(end, begin - 1, -1):
            item.append(x)
        return item
    return reverse_range(begin, end)

    # print(list(range(end, begin-1, -1)))


# reverse_range(1, 1)  # [1]
print(reverse_range(1, 5))  # [3, 2, 1]


def filter_positive(item):
    if item == []:
        return []
    for x, i in enumerate(item):

        if i < 0:
            item.pop(x)
            return item

    return filter_positive(item)


print(filter_positive([]))  # []
print(filter_positive([-3]))  # []
print(filter_positive([1, -2, 3]))  # [1, 3]

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
