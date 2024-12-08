"""Представьте, что берутся числа от 1 до n и соединяются в одну большую
строку. Как много цифр между 0 и n? Создать функцию, которая рассчитывает
это."""


def solution(n: int) -> int:
    string = ''

    for i in range(1, n):
        string += str(i)

    return len(string)


print(9 == solution(10))
print(189 == solution(100))
print(6973 == solution(2021))
