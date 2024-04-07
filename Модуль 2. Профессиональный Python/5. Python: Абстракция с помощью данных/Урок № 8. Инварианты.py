import math

"""Реализуйте абстракцию для работы с рациональными числами, которая включает
в себя следующие функции:

    - конструктор make — принимает на вход числитель и знаменатель,
    возвращает дробь;
    - селектор get_numer — возвращает числитель;
    - селектор get_denom — возвращает знаменатель;
    - сложение add — складывает переданные дроби;
    - вычитание sub — находит разность между двумя дробями.

Не забудьте реализовать нормализацию дробей удобным для вас способом.

Примеры работы:"""

# import rational
#
# rat1 = rational.make(3, 9)
# rational.get_numer(rat1)  # 1
# rational.get_denom(rat1)  # 3
# rat2 = rational.make(10, 3)
# rat3 = rational.add(rat1, rat2)
# rational.to_str(rat3)  # 11/3
# rat4 = rational.sub(rat1, rat2)
# rational.to_str(rat4)  # -3/1

"""Подсказки
    - функция gcd из модуля math находит наибольший общий делитель двух чисел;
    - функция to_str возвращает строковое представление числа (используется 
    для отладки);
    - функция int преобразует значение к целому числу."""


def make(numerator, denominator):
    gcd = math.gcd(numerator, denominator)
    return {
        "numerator": int(numerator / gcd),
        "denominator": int(denominator / gcd)
    }


def get_numer(fraction):
    return fraction["numerator"]


def get_denom(fraction):
    return fraction["denominator"]


def add(fraction_1, fraction_2):
    numer_1 = get_numer(fraction_1)
    denom_1 = get_denom(fraction_1)
    numer_2 = get_numer(fraction_2)
    denom_2 = get_denom(fraction_2)
    return make(numer_1 * denom_2 + numer_2 * denom_1, denom_1 * denom_2)


def sub(fraction_1, fraction_2):
    numer_1 = get_numer(fraction_1)
    denom_1 = get_denom(fraction_1)
    numer_2 = get_numer(fraction_2)
    denom_2 = get_denom(fraction_2)
    return make(numer_1 * denom_2 - numer_2 * denom_1, denom_1 * denom_2)


def to_str(fraction):
    return f'{get_numer(fraction)}/{get_denom(fraction)}'


'SOLUTION'
# def make(numer, denom):
#     gcd = math.gcd(numer, denom)
#     return {
#         "numer": int(numer / gcd),
#         "denom": int(denom / gcd),
#     }
#
#
# def get_numer(rat):
#     return rat["numer"]
#
#
# def get_denom(rat):
#     return rat["denom"]
#
#
# def add(rat1, rat2):
#     numer1 = get_numer(rat1)
#     denom1 = get_denom(rat1)
#     numer2 = get_numer(rat2)
#     denom2 = get_denom(rat2)
#
#     return make(
#         numer1 * denom2 + numer2 * denom1,
#         denom1 * denom2,
#     )
#
#
# def sub(rat1, rat2):
#     numer1 = get_numer(rat1)
#     denom1 = get_denom(rat1)
#     numer2 = get_numer(rat2)
#     denom2 = get_denom(rat2)
#
#     return make(
#         numer1 * denom2 - numer2 * denom1,
#         denom1 * denom2,
#     )


# print(make(3, 4))
#
# print(get_numer(make(3, 4)))
rat1 = make(3, 9)
# print(to_str(rat1))
print(get_numer(rat1))  # 1
print(get_denom(rat1))  # 3

rat2 = make(10, 3)
rat3 = add(rat1, rat2)
# print(rat3)
print(to_str(rat3))  # 11/3
rat4 = sub(rat1, rat2)
print(to_str(rat4))  # -3/1
