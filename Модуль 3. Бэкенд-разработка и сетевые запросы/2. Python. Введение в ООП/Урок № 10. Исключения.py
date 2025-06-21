"""Реализуйте декоратор suppress ("подавлять"), который должен перехватывать
заданное исключение (одно или кортеж), если таковое возникнет при вызове
оборачиваемой функции, и возвращать вместо ошибки заданное значение
(keyword-only аргумент "or_return", значение по умолчанию — None)."""


def suppress(exception, *, or_return=None):
    def wrapper(function):
        def inner(*args, **kwargs):
            try:
                return function(*args, **kwargs)
            except exception:
                return or_return
        return inner
    return wrapper


'SOLUTION'


# def suppress(exception, *, or_return=None):
#     def wrapper(function):
#         def inner(*args, **kwargs):
#             try:
#                 return function(*args, **kwargs)
#             except exception:
#                 return or_return
#
#         return inner
#
#     return wrapper


@suppress(ZeroDivisionError, or_return=42)
def foo():
    return 1 // 0


print(foo())  # 42


@suppress((KeyError, IndexError))
def get_item(key, structure):
    return structure[key]


print(get_item(7, "foo") is None)  # True
print(get_item('a', {}) is None)  # True
