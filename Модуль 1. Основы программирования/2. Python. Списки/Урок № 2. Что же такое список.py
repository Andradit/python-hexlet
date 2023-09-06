"""Реализуйте функцию is_list(), которая проверяет, является ли значение
списком.

Подсказки
Тип объекта можно проверить с помощью функции isinstance()
Список имеет тип list"""

# BEGIN (write your solution here)


def is_list(text):
    return isinstance(text, list)
# END


list_of_nums = [1, 2, 3]  # создаём список

print(is_list(list_of_nums))  # True
print(is_list('string'))  # False
