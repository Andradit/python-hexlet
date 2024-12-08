"""Напишите тесты для функции take(items, n), которая возвращает первые n
элементов из списка:"""

# Стандартный вызов функции
# take([1, 2, 3], 2)  # [1, 2]
#
# # По умолчанию функция возвращает один элемент
# take([1, 2, 3])  # [1]
#
# # Пытаемся извлечь больше элементов, чем содержит массив
# take([4, 3], 9)  # [4, 3]
#
# # Выбираем элементы из пустого массива
# take([], 2)  # []
#
# # Не извлекаем ни одного элемента
# take([1, 2, 3], 0)  # []

from functions import get_function

take = get_function()

assert take(['1', [2], 5], 2) == ['1', [2]]
assert take([{"key": 1}, 2, [5]]) == [{"key": 1}]
assert take([4, 3], 9) == [4, 3]
assert take([], 2) == []
assert take([1, 2, 3], 0) == []

'SOLUTION'
# assert take(['one', 'two', 8], 9) == ['one', 'two', 8]
# assert take([1, 2]) == [1]
# assert take(['one', 'two', 'three'], 2) == ['one', 'two']
# assert take(['one', 'two', 'three'], 0) == []
# assert take([]) == []