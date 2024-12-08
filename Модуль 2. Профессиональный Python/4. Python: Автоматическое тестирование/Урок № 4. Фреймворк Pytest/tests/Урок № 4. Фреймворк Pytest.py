"""Напишите тесты для функции without(coll, *values). Эта функция должна
принимать список в качестве первого параметра, а затем возвращать его копию,
из которой исключены значения, переданные вторым и последующими параметрами.
Если список содержит несколько одинаковых исключаемых элементов,
то исключаются они все:"""

from functions import get_function

# without = get_function()
#
# without([2, 1, 2, 3, 4], 2, 3)  # [1, 4]
# without([], 2)  # []

without = get_function()

def test_without():
    assert without([{'key': 1}, 4, 'A', []], {'key': 1}, 'A', []) == [4]
    assert without([1, 'B', [{'key': []}], 'B', 1], 1, 'B') == [[{'key': []}]]
    assert without(['D']) == ['D']

'SOLUTION'
def test_without():
    assert without([], 5) == []
    assert without([1, 2, 4, 5, 4, 7, 4], 4, 2) == [1, 5, 7]

