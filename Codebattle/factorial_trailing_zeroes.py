"""Вернуть количество конечных нулей в n! Например, 5! = 120 - число конечных
нулей - 1, 10! = 3 628 800 - число конечных нулей - 2"""

from math import factorial


def solution(n: int) -> int:
    result = 0
    for i in str(factorial(n))[::-1]:
        if i == '0':
            result += 1
        else:
            return result


print(6 == solution(28))
print(0 == solution(0))
print(1 == solution(5))
print(1 == solution(7))
print(4 == solution(23))
print(22 == solution(99))
