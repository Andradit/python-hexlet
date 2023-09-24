import zlib

'''Реализуйте и экспортируйте набор функций для работы с ассоциативным
массивом. Чтобы было проще, наша реализация не поддерживает разрешение
коллизий.

В этом задании надо реализовать словарь. По понятным причинам использовать
встроенные словари нельзя. Представьте, что в языке словарей нет, и мы их
хотим добавить.

- set_(map, key, value) — устанавливает в массив значение по ключу. Работает и
для создания, и для изменения. Функция возвращает True, если удалось
установить значение. При возникновении коллизии функция никак не меняет массив
и возвращает False
- get_(map, key, default = None) — возвращает значение указанного ключа.
Параметр default — значение, которое функция возвращает, если в словаре нет
ключа (по умолчанию равно None). При возникновении коллизии функция также
возвращает значение по умолчанию'''
# map = make()
# result = get_(map, 'key')
# print(result) ## => None

# result = get_(map, 'key', 'default')
# print(result) ## => default

# set_(map, 'key2', 'value2')  # True
# result = get_(map, 'key2')
# print(result) ## => value2

'''Подсказки

Для внутреннего представления словаря, используйте массив, где индекс содержит
хеш записи, а значение — кортеж (key, value)
Коллизии возникают, когда хеш одинаковый, а ключи — разные
Документация crc-32
Функция make() возвращает список, поддерживающий добавление и получение
элементов по несуществующим еще индексам. На место отсутствующих элементов
подставится None. А если попробовать получить элемент по несуществующему
индексу, то также вернется None'''
# m = make()
# m[2] = 5
# print(m)  # => [None, None, 5]
# m[42]  # None


class Map(list):
    def __setitem__(self, index, value):
        try:
            super().__setitem__(index, value)
        except IndexError:
            for _ in range(index - len(self) + 1):
                self.append(None)
            super().__setitem__(index, value)

    def __getitem__(self, index):
        try:
            return super().__getitem__(index)
        except IndexError:
            return None


def make():
    return Map()

# def get_hash(key):
#     return sum(ord(ch) for ch in key) % 10 + 1


def set_(map, key, value):
    hash = zlib.crc32(key)
    index = abs(hash) % 10
    if map[index] is None:
        map[index] = (key, value)
        return True
    else:
        if map[index][0] == key:
            map[index] = (key, value)
            return True
        else:
            return False


def get_(map, key, default=None):
    hash = zlib.crc32(key)
    index = abs(hash) % 10
    if map[index] is None:
        return default
    else:
        if map[index][0] == key:
            return map[index][1]
        else:
            return default

# SOLUTION
# def get_index(key):
#     return zlib.crc32(key) % 1000


# def has_collision(map, key):
#     index = get_index(key)
#     current_key, _ = map[index]
#     return current_key != key


# def set_(map, key, value):
#     index = get_index(key)
#     if map[index] and has_collision(map, key):
#         return False
#     map[index] = (key, value)
#     return True


# def get_(map, key, default=None):
#     index = get_index(key)
#     if (not map[index]) or has_collision(map, key):
#         return default
#     _, value = map[index]
#     return value

map = make()
print(get_(map, b'key'))  # None
# assert get_(map, b'key') == None

print(get_(map, b'key', b'value'))  # b'value'

print(set_(map, b'key2', b'value2'))  # True
print(get_(map, b'key2'))  # b'value2'

print(get_(map, b'None'))  # None

print(set_(map, b'key2', b'another value'))  # False
print(map)
assert get_(map, b'key2') == b'another value'
print(get_(map, b'key2'))  # b'another value'


print(set_(map, b'aaaaa0.462031558722291', b'vvv'))  # True
print(set_(map, b'aaaaa0.0585754039730588', b'boom!'))  # False

print(get_(map, b'aaaaa0.462031558722291'))  # b'vvv'

print(get_(map, b'aaaaa0.0585754039730588'))  # None

print(set_(map, b'aaaaa0.462031558722291', b'wop'))  # False
print(get_(map, b'aaaaa0.462031558722291'))  # b'wop'
