"""Цель данного упражнения — реализовать функцию find_second_index(). В этом упражнении вам пригодится функция find_index(), которую вы реализовали в прошлом упражнении. Напоминаю, эта функция возвращает индекс первого элемента последовательности, равного заданному значению. Функция find_second_index() же должна возвращать индекс второго подходящего элемента в последовательности. Если подходящих элементов в последовательности меньше двух или же последовательность пуста, нужно всё так же возвращать None.

Новую функцию вам следует реализовывать с помощью уже имеющейся find_index(). И не забудьте, что итератор сохраняет позицию, в которой остановился обход — это знание поможет вам в решении поставленной задачи!"""


def find_first_index(value, items):
    for (index, item) in enumerate(items):
        # print(f"{index=},{item=},{value=}")
        if value == item:
            return index

def find_second_index(value, items):
    it = iter(items)
    first_index = find_first_index(value, it)
    # print(f"{first_index=}")
    second_index = find_first_index(value, it)
    if second_index is None:
        return None
    return second_index + first_index + 1

# def find_second_index(value, items): ---> solution
#     iterator = iter(items)
#     first = find_index(value, iterator)
#     if first is None:
#         return first
#     second = find_index(value, iterator)
#     if second is not None:
#         return first + second + 1

# def find_second_index(value, items):
#     first_index = items.find(value)
#     second_index = items.find(value, first_index + 1)
#     if second_index == -1:
#         return None
#     return second_index

# a = 'Hello'
# print(a.index())

# it = iter('Hello')
# print(next(it))
# print(next(it))
print(find_second_index('b', 'bob'))  # 2

print(find_second_index('a', 'cat')) is None  # True

print(find_second_index('a', '')) is None  # True

print(find_second_index('l', 'Hello'))
