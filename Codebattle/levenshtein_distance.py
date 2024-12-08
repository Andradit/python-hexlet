"""Рассчитать расстояние Левенштейна"""


def solution(s1: str, s2: str) -> int:
    size_x = len(s1) + 1
    size_y = len(s2) + 1

    matrix = [[0] * size_y for _ in range(size_x)]

    for x in range(size_x):
        matrix[x][0] = x
    for y in range(size_y):
        matrix[0][y] = y

    for x in range(1, size_x):
        for y in range(1, size_y):
            if s1[x - 1] == s2[y - 1]:
                substitution_cost = 0
            else:
                substitution_cost = 1

            matrix[x][y] = min(
                matrix[x - 1][y] + 1,  # deletion
                matrix[x][y - 1] + 1,  # insertion
                matrix[x - 1][y - 1] + substitution_cost  # substitution
            )

    return matrix[size_x - 1][size_y - 1]


'ALTERNATIVE SOLUTION'
# pip install python-Levenshtein
#
# import Levenshtein as lev
#
# distance = lev.distance('kitten', 'sitting')
# print(distance)  # Outputs: 3


print(solution('kitten', 'sitting'))  # 3
print(solution('clojure', 'closure'))  # 1
print(solution('xyx', 'xyyyx'))  # 2
print(solution('', '123456'))  # 6
