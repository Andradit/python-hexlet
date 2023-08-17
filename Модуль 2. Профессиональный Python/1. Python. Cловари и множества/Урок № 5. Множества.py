'''Вам предстоит реализовать функцию all_unique(). Эта функция должна:

Принимать итерируемый объект или итератор (в том числе и не перезапускаемые)
Возвращать True, если элементы не повторяются (если элементов нет, то ничего
не повторяется)
Посмотрим на пример работы этой функции:

all_unique([])
# True
all_unique([1, 2, 3])
# True
all_unique(iter([1, 2, 3]))
# True
all_unique([1, 2, 1])
# False
'''


def all_unique(elements):
    iter_list = list(elements)
    # print(iter_list)
    # print(list(elements))
    if len(set(iter_list)) == len(iter_list):
        return True
    else:
        return False


print(all_unique([]))  # True
print(all_unique([1, 2, 3]))  # True
print(all_unique(iter([1, 2, 3])))  # True
print(all_unique([1, 2, 1]))  # False
