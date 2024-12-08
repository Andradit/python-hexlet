import os

import right
import wrong1
import wrong2
import wrong3


def get_validator():
    name = os.environ['FUNCTION_VERSION']
    return {
        "right": right,
        "wrong1": wrong1,
        "wrong2": wrong2,
        "wrong3": wrong3,
    }[name].make_validator
