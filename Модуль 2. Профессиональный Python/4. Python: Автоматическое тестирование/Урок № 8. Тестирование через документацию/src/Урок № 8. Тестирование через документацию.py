"""Напишите doctests для функции invert_case(). Тесты должны содержать три
разных кейса."""

def invert_case(string):
    # BEGIN (write your solution here)
    """Invert case

    >>> invert_case('StRIng')
    'sTriNG'

    >>> invert_case('STRING')
    'string'

    >>> invert_case('string')
    'STRING'
    """
    # END

    result = ''
    for char in string:
        result += char.swapcase()
    return result


if __name__ == "__main__":
    import doctest
    failed, attempted = doctest.testmod()
    assert failed == 0
    assert attempted == 3