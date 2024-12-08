import re

"""Даны предложение и слово, найти все местоположения слова в предложении и
собрать их в массив"""


def solution(sentence: str, word: str) -> list[int]:
    result = []
    match = re.finditer(rf'\b{word}\b', rf'{sentence}')

    for elem in match:
        result.append(elem.start())
    return result


# print(solution("find a word in some sentence in all text", "in"))
# print(solution("tester, test, tested", "test"))
# print(solution("test test test", "test"))

print([12] == solution("find a word in some sentence", "in"))
print([0] == solution("test", "test"))
print([0, 5, 10] == solution("test test test", "test"))
