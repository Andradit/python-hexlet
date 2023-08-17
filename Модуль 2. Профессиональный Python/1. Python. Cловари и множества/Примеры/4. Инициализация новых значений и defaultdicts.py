from collections import defaultdict

# Если хранить в словаре в качестве значений списки или любые другие
# изменяемые данные
dictionary = {}
key = 'name'
value = 'John'
if key not in dictionary:
    dictionary[key] = []  # инициализируем список
dictionary[key].append(value)

print(dictionary)

# setdefault принимает ключ и значение по умолчанию, а затем возвращает ссылку
# на значение в словаре, связанное с указанным ключом. Если ключ в словаре
# отсутствует, то метод помещает по ключу то самое значение по умолчанию и
# возвращает ссылку на него.
dictionary.setdefault(key, []).append(value)

print(dictionary)

# модуль collections - предоставляет тип defaultdict
# Обычный словарь ругается на отсутствие ключа, а defaultdict сам возвращает
# значение по умолчанию

d = defaultdict(int)
d['a'] += 5
d['b'] = d['c'] + 10
print(d)  # defaultdict(<class 'int'>, {'a': 5, 'c': 0, 'b': 10})


def new_value():
    return 'foo'


x = defaultdict(new_value)
print(x[1])  # 'foo'
print(x['bar'])  # 'foo'
print(x)  # defaultdict(<function new_value at 0x7fd054bf93a0>, {1: 'foo',
# 'bar': 'foo'})
