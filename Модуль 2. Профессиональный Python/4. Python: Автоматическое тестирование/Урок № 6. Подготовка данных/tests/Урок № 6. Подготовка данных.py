"""Напишите тесты для функции set_(coll, path, value). Эта функция возвращает
словарь, в котором она изменяет или добавляет значение по указанному пути.
Функция мутирует словарь:"""

# Все вызовы нужно рассматривать, как независимые
# coll = {'a': {'b': {'c': 3}}}
# set_(coll, ['a', 'b', 'c'], 4)
# coll['a']['b']['c']  # 4
# set_(coll, ['x', 'y', 'z'], 5)
# coll['x']['y']['z']  # 5
# set_(coll, ['a', 'b', 'd'], 7)
# coll['a']['b']['d']  # 7
# coll['a']['b']['c']  # 3

"""Подсказки
    - переиспользуйте объект данных;
    - тесты не должны зависеть друг от друга;
    - помните, что неверная реализация функции set_() может возвращать 
    словарь с неправильной структурой."""

import pytest
import copy

from functions import get_function

set_ = get_function()

@pytest.fixture
def coll():
    return {'a': {'b': {'c': 3}}}

def test_set_1(coll):
    data_copy = copy.deepcopy(coll)
    set_(coll, ['c'], 'x')
    data_copy['c'] = 'x'
    assert data_copy == coll


def test_set_2(coll):
    data_copy = copy.deepcopy(coll)
    set_(coll, ['a', 'b', 'c'], 4)
    data_copy['a']['b']['c'] = 4
    assert data_copy == coll


def test_set_3(coll):
    data_copy = copy.deepcopy(coll)
    set_(coll, ['a', 'b', 'd'], 7)
    data_copy['a']['b']['d'] = 7
    assert data_copy == coll

