"""Дан массив слов. Написать функцию, которая картинку (массив) с границей из
звёздочек *. Внутри границы находятся самые длинные слова."""


def solution(words: list[str]) -> list[str]:
    result = ['*']

    for word in words:
        if len(max(words, key=len)) == len(word):
            result.append('*' + word + '*')
            result[0] = '*' * (len(word) + 2)
    result.append(result[0])

    return result


print(solution(['a', 'bc', 'bbb', 'aaa', 'sss']))
