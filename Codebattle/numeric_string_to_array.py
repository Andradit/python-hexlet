"""Сконвертировать числовую строку в массив чисел. Гарантируется,
что строковое число не отрицательное"""


def solution(string: str) -> list[int]:
    split_string = list(string)
    return list(map(lambda x: int(x), split_string))


print([1, 2, 3] == solution('123'))
print([3, 0, 9, 0, 2] == solution('30902'))
print([1, 0, 1, 0, 0] == solution('10100'))
