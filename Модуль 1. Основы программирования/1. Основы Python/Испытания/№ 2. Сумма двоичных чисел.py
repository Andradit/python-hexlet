"""Это испытание требует знакомства с двоичной системой счисления.

Реализуйте функцию binary_sum(), которая принимает на вход два двоичных числа в виде строк и возвращает их сумму. Вычисленная сумма также должна быть бинарным числом в виде строки:

binary_sum('10', '1')      # 11
binary_sum('1101', '101')  # 10010

Подсказки
Синтаксис форматирования строк
int()"""


def binary_sum(a, b):
    sum = int(a, 2) + int(b, 2)
    # return "{0:b}".format(sum)
    return f"{sum:b}"

# def binary_sum(number_a, number_b): #---> solution
#     binary_a = int(number_a, base=2)
#     binary_b = int(number_b, base=2)
#     return f'{binary_a + binary_b:b}'


print(binary_sum('10', '1'))      # 11
print(binary_sum('1101', '101'))  # 10010


# print("bin: {0:d}".format(1100))

# a = '1100'
# # a = int(a)
# print(int(a, 2))
