"""Треугольник Паскаля — бесконечная таблица биномиальных коэффициентов, имеющая треугольную форму. В этом треугольнике на вершине и по бокам стоят единицы. Каждое число равно сумме двух расположенных над ним чисел. Строки треугольника симметричны относительно вертикальной оси.

0:      1
1:     1 1
2:    1 2 1
3:   1 3 3 1
4:  1 4 6 4 1
src/solution.py
Напишите функцию triangle(), которая возвращает указанную строку треугольника Паскаля в виде списка.

Подсказки
Треугольник Паскаля представляет собой таблицу коэффициентов бинома Ньютона, который в свою очередь применяется в теории вероятности и вычислении числа e. Также треугольник Паскаля частая задачка на интервью."""

# BEGIN (write your solution here)
from math import factorial


def triangle(n):
    list = []
    for char in range(n):
        result = factorial(n) / (factorial(char) * factorial(n - char))
        list.append(result)
    list.append(1)
    return list




# END
print(triangle(0))  # [1]
print(triangle(1))  # [1, 1]
print(triangle(2))  # [1, 2, 1]
print(triangle(3))  # [1, 3, 3, 1]
print(triangle(4))  # [1, 4, 6, 4, 1]

# BEGIN -----> soluton
# Определяем функцию для вычисления факториала
# def fact(n):
#     if n == 0:
#         return 1
#     return n * fact(n - 1)


# def triangle(row_number):
#     numbers_count = row_number + 1
#     line = []
#     calculated = fact(row_number)
#     for i in range(numbers_count):
#         # Для вычисления числа заданной строки используем формулу
#         # расчёта биноминальных коэффициентов С(n, k) = n! / (k! * (n - k)!)
#         line.append(calculated / (fact(i) * fact(row_number - i)))
#     return line


# Alternative solutions
#
# def triangle(row):
#     line = [1]
#     for i in range(row):
#         line.append(line[i] * ((row - i) / (i + 1)))
#     return line
#
#
# from operator import add


# def triangle(row_number):
#     row = [1]
#     for _ in range(row_number):
#         row = list(map(  # [x,y,z]
#             add,         # x y z 0
#             row + [0],   # + + + +
#             [0] + row,   # 0 x y z
#         ))
#     return row
# END

# print(triangle(0))  # [1]
# print(triangle(1))  # [1, 1]
# print(triangle(2))  # [1, 2, 1]
# print(triangle(3))  # [1, 3, 3, 1]
# print(triangle(4))  # [1, 4, 6, 4, 1]
