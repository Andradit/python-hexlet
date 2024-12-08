import os


def _right(coll, *values):
    return [item for item in coll if item not in values]


def _fail1(coll, *values):
    result = [item for item in coll if item not in values]
    return None if result else result


def _fail2(coll, *values):
    excluded = []
    result = []
    for element in coll:
        if element not in values:
            result.append(element)
        elif element in excluded:
            result.append(element)
        else:
            excluded.append(element)
    return result


functions = {
    "right": _right,
    "fail1": _fail1,
    "fail2": _fail2,
}


def get_function():
    name = os.environ['FUNCTION_VERSION']
    return functions[name]
