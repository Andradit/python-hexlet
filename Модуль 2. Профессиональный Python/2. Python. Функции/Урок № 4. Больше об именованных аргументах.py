'''Цель данного упражнения — функция updated(). Эта функция должна принимать
словарь в качестве единственного позиционного аргумента (обязательного) и
произвольное кол-во именованных аргументов. Возвращать же функция должна новый
словарь, в котором ключи, соответствующие именованным аргументам, должны иметь
сопутствующие значения (см.примеры).'''

# d = {'a': 1, 'b': False}
# updated(d, a=2, b=True, c=None) => {'a': 2, 'b': True, 'c': None}
# print(d) => {'a': 1, 'b': False}
# updated(d) == d
# # True
# updated(d) is d
# False


def updated(d, **kwargs):
    dict = d.copy()
    dict.update(kwargs)
    return dict

# SOLUTION
# def updated(dictionary, **kwargs):
#     new = dictionary.copy()
#     new.update(kwargs)
#     return new


old = {'a': 1, 'b': None, 2: 4}
copy_of_old = old.copy()
print(updated(old) is not old)  # True
print(updated(old, a=2))  # {'a': 2, 'b': None, 2: 4}
print(old == copy_of_old, "Old dict should stay unchanged!")
print(updated({}, foo='bar', bar=42))  # {'foo': 'bar', 'bar': 42}
