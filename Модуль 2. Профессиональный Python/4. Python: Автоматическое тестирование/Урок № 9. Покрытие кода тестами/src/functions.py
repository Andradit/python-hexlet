import os

import right
import wrong1
import wrong2
import wrong3

functions = {
    "right": {
        "get": right.get,
        "index_of": right.index_of,
        "slice": right.my_slice,
    },
    "wrong1": {
        "get": wrong1.get,
        "index_of": wrong1.index_of,
        "slice": wrong1.my_slice,
    },
    "wrong2": {
        "get": wrong2.get,
        "index_of": wrong2.index_of,
        "slice": wrong2.my_slice,
    },
    "wrong3": {
        "get": wrong3.get,
        "index_of": wrong3.index_of,
        "slice": wrong3.my_slice,
    },
}


def get_functions():
    name = os.environ["FUNCTION_VERSION"]
    return functions[name]