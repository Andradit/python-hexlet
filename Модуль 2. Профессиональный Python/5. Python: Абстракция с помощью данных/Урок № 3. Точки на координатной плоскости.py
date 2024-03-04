"""Реализуйте функцию calculate_distance(), которая находит расстояние между
двумя точками на плоскости:"""

# point1 = [0, 0]
# point2 = [3, 4]
# calculate_distance(point1, point2)  # 5.0

"""Подсказки

Расстояние между точками вычисляется по формуле: d = √((x₂−x₁)²+(y₂−y₁)²)
Объяснение формулы расчёта расстояния между двумя точками"""


def calculate_distance(point_1, point_2):
    x1, y1 = point_1
    x2, y2 = point_2
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


'SOLUTION'

# import math
#
# def calculate_distance(point1, point2):
#     delta_x = point2[0] - point1[0]
#     delta_y = point2[1] - point1[1]
#
#     return math.sqrt((delta_x ** 2) + (delta_y ** 2))


point1 = [0, 0]
point2 = [3, 4]
print(calculate_distance(point1, point2))  # 5.0
print(calculate_distance([-1, -4], [-1, -10]))  # 6.0
print(calculate_distance([1, 10], [1, 3]))  # 7.0
