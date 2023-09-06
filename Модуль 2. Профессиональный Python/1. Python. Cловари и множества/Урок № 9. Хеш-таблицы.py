'''Реализуйте функцию get_or_default(). Она должна возвращать из хеш-таблицы
значение по ключу или значение по умолчанию, если такой записи не существует
'''

# m = make_map()
# # метод set(ключ, значение) записывает значение по ключу в мапу
# m.set("g", "bar")
# m.set("e", "foo")

# get_or_default(m, "g", "python") # bar
# get_or_default(m, "a", "python") # python

'''Хеш-таблица представляет собой список, содержащий пары (ключ, значение) по
индексам. Индексы рассчитываются из результата применения хеш-функции
get_hash() к ключу. Если записи по такому индексу еще нет, то вместо пары
хранится None.'''

# get_hash('e') # 2
# get_hash('f') # 3
# get_hash('g') # 4

# m = make_map()
# m.set("e", "foo")
# m.set("f", "baz")
# m.set("g", "bar")

# print(m) # => [None, None, ('e', 'foo'), ('f', 'baz'), ('g', 'bar')]
'''Подсказки
Функция получения хеша get_hash() уже импортирована
Вы можете посмотреть устройство make_map() в модуле map.py'''


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

    def set(self, key, value):
        index = get_hash(key)
        self[index] = (key, value)


def make_map():
    return Map()


def get_hash(key):
    return sum(ord(ch) for ch in key) % 10 + 1


map = make_map()
# def get_or_default(map, key, value):
#     print(get_hash(key))
#     print(map)
#     index = get_hash(key)
#     if map[index] is None:
#         return value
#     return map[index][1]


def get_or_default(map, key, value):
    return value if map[get_hash(key)] is None else map[get_hash(key)][1]

# SOLUTION
# def get_or_default(map, key, default):
#     index = get_hash(key)
#     data = map[index]
#     if data is None:
#         return default
#     _, value = data
#     return value


map.set("e", "foo")
map.set("f", "baz")
map.set("g", "bar")
print(map)
map.set('o', 'yes')
print(map)
# print(get_or_default(map, "e", "python")) # foo
# print(get_or_default(map, "g", "python")) # bar
# print(get_or_default(map, "a", "python")) # python

# map.set("e", "hello")
# map.set("k", "world")
# map.set("m", "python")
# print(map)
# print(get_or_default(map, "e", "bar")) # "hello"
# print(get_or_default(map, "k", "k")) # "world"
# print(get_or_default(map, "f", "foo")) # "foo"

# get_or_default(map, 'e', 'foo')
# get_or_default(map, 'n', 'baz')
# get_or_default(map, 'o', 'foo')
