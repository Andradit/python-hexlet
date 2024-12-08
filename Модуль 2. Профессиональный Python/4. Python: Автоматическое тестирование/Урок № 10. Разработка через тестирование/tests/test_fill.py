import os

import pytest

import right
import solution
import wrong1
import wrong2
import wrong3


@pytest.fixture(name='fill')
def _fill():
    name = os.environ['FUNCTION_VERSION']
    return {
        "user_implementation": solution,
        "right": right,
        "wrong1": wrong1,
        "wrong2": wrong2,
        "wrong3": wrong3,
    }[name].fill


@pytest.fixture(name='collection')
def _collection():
    return [1, 2, 3, 4]


def test_fill(collection, fill):
    fill(collection, '*', 1, 3)
    assert collection == [1, '*', '*', 4]


# BEGIN (write your solution here)
def test_fill_default(collection, fill):
    fill(collection, '*')
    assert collection == ['*', '*', '*', '*']


def test_fill_no_end(collection, fill):
    fill(collection, '*', 5)
    assert collection == [1, 2, 3, 4]


def test_fill_overlength(collection, fill):
    fill(collection, '*', 0, 8)
    assert collection == ['*', '*', '*', '*']
# END

# def test_fill_default(collection, fill):
#     fill(collection, '*')
#     assert collection == ['*', '*', '*', '*']
#
#
# def test_fill_start_ge_length(collection, fill):
#     fill(collection, '*', 10, 12)
#     assert collection == [1, 2, 3, 4]
#
#
# def test_fill_start_ge_end(collection, fill):
#     fill(collection, '*', 2, 2)
#     assert collection == [1, 2, 3, 4]
#
#
# def test_fill_end_ge_length(collection, fill):
#     fill(collection, '*', 0, 10)
#     assert collection == ['*', '*', '*', '*']