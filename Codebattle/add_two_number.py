"""Посчитать сумму цифр целого числа n"""


def solution(n: int) -> int:
    return sum([int(i) for i in str(n)])


print(solution(12))
print(3 == solution(12))
print(18 == solution(99))
