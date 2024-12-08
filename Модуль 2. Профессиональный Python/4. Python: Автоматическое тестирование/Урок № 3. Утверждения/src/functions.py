import os


def _right(collection, length=1):
    return collection[:length]


def _wrong1(collection, length=1):
    return collection[length, 0]


def _wrong2(collection, length=1):
    if length >= len(collection):
        return []
    return collection[:length]


def _wrong3(collection, length=5):
    return collection[:length]


def _wrong4(collection, length=1):
    if not collection:
        return [0]
    return collection[:length]


functions = {
    "right": _right,
    "wrong1": _wrong1,
    "wrong2": _wrong2,
    "wrong3": _wrong3,
    "wrong4": _wrong4,
}


def get_function():
    name = os.environ['FUNCTION_VERSION']
    return functions[name]
