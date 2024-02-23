"""Вам предстоит реализовать три функции. Каждая функция будет работать с
двухмерной матрицей, то есть со списком списков (итератором итераторов):

    - функция each2d(test, matrix) должна проверить, что каждый элемент матрицы
    matrix удовлетворяет предикату test. Она должна вернуть False, если test
    вернул False хотя бы для одного элемента. В противном случае функция должна
    возвращать True;

    - функция some2d(test, matrix) должна проверить, удовлетворяет ли предикату
    test хотя бы один элемент матрицы matrix. Как только test возвращает True
    для какого-либо элемента, функция должна вернуть True. Если ни один элемент
    проверку не прошел, нужно вернуть False;

    - функция sum2d(test, matrix) должна возвращать сумму всех элементов матрицы
    matrix, удовлетворяющих предикату test.

Первые две функции не должны выполнять лишней работы. Другими словами,
обход матрицы должен прерываться, как только результат становится ясен:

Подсказки
- функция all(xs) проверяет, что среди элементов xs нет ни одного False;
- функция any(xs) проверяет, что среди элементов xs есть хотя бы один True;
- функция sum(xs) возвращает сумму элементов xs."""


def is_int(x):
    return isinstance(x, int)


# each2d(is_int, [[1, 2], [3, 4]])  # True
# each2d(is_int, [[1, None], [3, 4]])  # False

# # В пустой матрице нет ни одного элемента, который бы завалил тест
# each2d(is_int, [])  # True
#
# some2d(is_int, [[None, "foo"], [(), {}]])  # False
# some2d(is_int, [[None, "foo"], [0, {}]])  # True

# # В пустой матрице нет ни одного элемента, который бы прошел тест
# some2d(is_int, [])  # False
#
# sum2d(is_int, [[1, "Foo", 100], [False, 10, None]])  # 111

def each2d(test, matrix):
    return all(test(cell) for row in matrix for cell in row)


def some2d(test, matrix):
    return any(test(cell) for row in matrix for cell in row)


def sum2d(test, matrix):
    return sum(cell for row in matrix for cell in row if test(cell))


"SOLUTION"

# def each2d(test, matrix):
#     return all(
#         test(cell)
#         for row in matrix
#         for cell in row
#     )
#
#
# def some2d(test, matrix):
#     return any(
#         test(cell)
#         for row in matrix
#         for cell in row
#     )
#
#
# def sum2d(test, matrix):
#     return sum(
#         cell
#         for row in matrix
#         for cell in row if test(cell)
#     )

print(each2d(is_int, [[1, 2], [3, 4]]))  # True
print(each2d(is_int, [[1, None], [3, 4]]))  # False
print(each2d(is_int, []), '\n')  # True

print(some2d(is_int, [[None, "foo"], [(), {}]]))  # False
print(some2d(is_int, [[None, "foo"], [0, {}]]))  # True
print(some2d(is_int, []), '\n')  # False

print(sum2d(is_int, [[1, "Foo", 100], [False, 10, None]]))  # 111

# print(any(x > 100 for x in range(1000000)))
