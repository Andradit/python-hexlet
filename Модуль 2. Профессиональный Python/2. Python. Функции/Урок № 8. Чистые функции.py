import math

'''Реализуйте функцию, которая проверяет переданное число на простоту и
печатает на экран yes или no.

Примеры'''

# say_prime_or_not(5) ## yes
# say_prime_or_not(4) ## no

'''Подсказки
Цель этой задачи — научиться отделять чистый код от кода с побочными эффектами.

Для этого выделите процесс определения того, является ли число простым, в
отдельную функцию, возвращающую логическое значение. Это функция, с помощью
которой мы отделяем чистый код от кода, интерпретирующего логическое значение
(как 'yes' или 'no') и делающего побочный эффект (печать на экран).

Пример такого разделения и хороших абстракций — в решении учителя.'''


def is_prime(num):
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
        elif num == 0 or num == 1:
            return False
    return True


def say_prime_or_not(number):
    if is_prime(number):
        print('yes')
    else:
        print('no')


say_prime_or_not(5)  # yes
say_prime_or_not(4)  # no


# SOLUTION
# def is_prime(num):
#     if num < 2:
#         return False
#     for i in range(2, int(math.sqrt(num)) + 1):
#         if num % i == 0:
#             return False
#     return True


# def say_prime_or_not(num):
#     answer = 'yes' if is_prime(num) else 'no'
#     print(answer)
