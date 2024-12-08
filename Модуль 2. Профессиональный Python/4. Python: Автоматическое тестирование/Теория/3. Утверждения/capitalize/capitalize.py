def capitalize(text):
    if text == '':
        return ''
    first_char = text[0].upper()
    rest_substring = text[1:]
    return f'{first_char}{rest_substring}'


def new_capitalize(text):
    first_char, *rest_chars = text
    rest_substring = ''.join(rest_chars)
    return f'{first_char.upper()}{rest_substring}'
