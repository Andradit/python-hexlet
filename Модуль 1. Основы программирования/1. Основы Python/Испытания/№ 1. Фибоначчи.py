"""Реализуйте функцию fib(), находящую положительные Числа Фибоначчи.
Аргументом функции является порядковый номер числа.
Формула:
f(0) = 0
f(1) = 1
f(n) = f(n-1) + f(n-2)

fib(3)  # 2
fib(5)  # 5
fib(10)  # 55"""


def fib(n):
    i = 0
    result = 0
    fn1 = 0
    fn2 = 1
    while i < n:
        # print(f"{i=},{n=},{result=},{fn1=},{fn2=}")
        result = sum([fn1, fn2])
        fn2 = fn1
        fn1 = result
        i += 1

    return result


# for n in range(0, 10):
#     print(fib(n))

print(fib(10))


# def fib(num):    -----> solution
#     if num == 0:
#         return 0

#     if num == 1:
#         return 1

#     first, second = 0, 1
#     result = first + second

#     index = 2
#     while index <= num:
#         result = first + second
#         first, second = second, result

#         index += 1

#     return result


# def fib(number):    ----> alternative solution
#     if number == 0:
#         return 0
#     elif number == 1:
#         return 1
#     else:
#         return fib(number - 1) + fib(number - 2)

# for n in range(0, 10):
#     print(fib(n))


# print(fib(10))
