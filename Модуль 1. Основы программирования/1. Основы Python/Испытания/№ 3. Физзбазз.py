"""Реализуйте функцию fizz_buzz, которая возвращает
строку с числами (через пробел) в диапазоне от begin до end включительно.
При этом:

Если число делится без остатка на 3, то вместо него выводится слово Fizz
Если число делится без остатка на 5, то вместо него выводится слово Buzz
Если число делится без остатка и на 3, и на 5, то вместо числа выводится слово
FizzBuzz
В остальных случаях в строку добавляется само число.
Функция принимает параметры begin и end, которые определяют начало и
конец диапазона включительно. Функция возвращает пустую строку, если
диапазон пуст — в случае, когда begin > end.

Пример
Вызов функции:

from solution import fizz_buzz
print(fizz_buzz(1, 5))
# => 1 2 Fizz 4 Buzz
print(fizz_buzz(11, 20))
# => 11 Fizz 13 14 FizzBuzz 16 17 Fizz 19 Buzz
Это задание крайне часто задают на собеседованиях."""


def fizz_buzz(begin, end):
    result = ''
    for n in range(begin, end+1):

        if n % 3 == 0 and n % 5 == 0:
            result += "FizzBuzz "
        elif n % 3 == 0:
            result += "Fizz "
        elif n % 5 == 0:
            result += "Buzz "
        elif begin > end:
            result += " "
        else:
            result += f"{n} "

    return result.rstrip()


print(fizz_buzz(2, 16))

# def fizz_buzz(start, stop): ---> solution
# result = ''
# while start <= stop:
#     if result:
#         result += ' '
#     if start % 15 == 0:
#         result += 'FizzBuzz'
#     elif start % 3 == 0:
#         result += 'Fizz'
#     elif start % 5 == 0:
#         result += 'Buzz'
#     else:
#         result += str(start)
#     start += 1
# return result
