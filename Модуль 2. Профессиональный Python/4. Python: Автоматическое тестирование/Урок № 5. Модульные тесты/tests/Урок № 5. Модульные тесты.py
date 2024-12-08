"""Напишите тесты для валидатора, который проверяет корректность данных.
Принцип работы валидатора следующий:

    1. С помощью функции add_check(fn) в валидатор добавляются проверки. Каждая
    проверка — это функция-предикат. Она принимает на вход проверяемое значение,
    а затем возвращает True или False в зависимости от того, соответствует ли
    значение требованиям проверки
    2. С помощью функции is_valid(value) пользователь проверяет соответствие
    значения всем добавленным проверкам. Если не было добавлено ни одной
    проверки, любое значение считается верным Сам валидатор выглядит так:"""

# from validators import get_validator
# make_validator = get_validator()
# add_check, is_valid = make_validator()
# is_valid("some value")  # True
# add_check(lambda x: x > 5)
# add_check(lambda x: x % 2 == 0)
# is_valid(3)  # False
# is_valid(4)  # False
# is_valid(7)  # False
# is_valid(8)  # True

"""Допишите уже существующий тест - добавьте в него проверки в валидатор и 
протестируйте их сочетания."""

from validators import get_validator

make_validator = get_validator()

add_check, is_valid = make_validator()
assert is_valid("value")

'MY SOLUTION'
add_check(lambda x: isinstance(x, int))
assert is_valid(9)
assert not is_valid("value")

add_check(lambda x: x > 5)
add_check(lambda x: x % 2 == 0)
assert is_valid(8)
assert not is_valid(2)
assert not is_valid(13)

# 'SOLUTION'
#
# add_check(lambda x: isinstance(x, int))
# assert is_valid(5)
# assert not is_valid("value")
#
# add_check(lambda x: x > 10)
# add_check(lambda x: x % 2 == 0)
# assert is_valid(12)
# assert not is_valid(8)
# assert not is_valid(21)
