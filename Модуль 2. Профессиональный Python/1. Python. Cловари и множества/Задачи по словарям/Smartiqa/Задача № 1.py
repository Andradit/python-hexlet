"""Напишите функцию to_dict(lst), которая принимает аргумент в виде списка и
возвращает словарь, в котором каждый элемент списка является и ключом и
значением. Предполагается, что элементы списка будут соответствовать правилам
задания ключей в словарях."""


def to_dict(lst):
    dict = {}
    for k in lst:
        dict[k] = k
    return dict


print(to_dict(['a', 5, 'b', 9, 'c', 11]))

# SOLUTION
# def to_dict(lst):
#     return {element: element for element in lst}
