# l = [1, 2, 3]
# l.pop(-2)  # 3
# print(l)

"""Вам нужно реализовать функцию rotate(), которая должна принимать список в качестве аргумента и перемещать последний элемент списка в начало списка. Функция должна изменять переданный список, а не возвращать новый. Если функция получает пустой список, то изменять его она не должна.

Подсказки
Для решения используйте методы insert() и pop()"""

# BEGIN (write your solution here)


def rotate(items):
    if items == []:
        return items
    items.insert(0, items.pop())
# END

# def rotate(items):  ---> solution
#     if items:
#         items.insert(0, items.pop())


items = [1, 2, 3, 5, 8]
rotate(items)
# items.extend([items[len(items) - 1]]) ---> pop()
print(items)  # => [8, 3, 1, 2, 5]
