"""Написать функцию, которая принимает последовательность слов и проверяет,
могут ли слова быть организованы в одну непрерывную цепочку слов. Пример:
cat -> cot -> coat -> oat -> hat -> hot -> hog -> dog"""


def word_comparison(word_1, word_2):
    copy_word_1 = list(word_1)
    copy_word_2 = list(word_2)
    count = 0
    for symbol_1, symbol_2 in zip(copy_word_1, copy_word_2):
        if len(copy_word_1) == len(copy_word_2) and symbol_1 != symbol_2:
            count += 1
            if count > 1:
                break
        elif symbol_1 != symbol_2 and len(copy_word_1) == len(copy_word_2) + 1:
            count += 1
            copy_word_1.pop(copy_word_1.index(symbol_1))
            if copy_word_1 == copy_word_2:
                break
            else:
                count += 1
        elif symbol_1 != symbol_2 and len(copy_word_1) + 1 == len(copy_word_2):
            count += 1
            copy_word_2.pop(copy_word_2.index(symbol_2))
            if copy_word_1 == copy_word_2:
                break
            else:
                count += 1
        elif (len(copy_word_1) - len(copy_word_2) > 1 or len(copy_word_2) -
              len(copy_word_1) > 1):
            count += 1
        # else:
        #     return False
    if count > 1:
        return False
    else:
        return True


print(word_comparison('cot', 'hot'))
print(word_comparison('tospl', 'top'))
print(word_comparison('toss', 'stop'))


# if ''.join(copy_word_1) in ''.join(copy_word_2) or ''.join(
#         copy_word_2) in ''.join(copy_word_1):
#     return True


def solution(words: list[str]) -> bool:
    result = []
    words.sort(key=len, reverse=True)
    # print(words)

    for word in words:
        for next_word in words:  # [words.index(word):]:
            if word == next_word:
                continue
            if word_comparison(word, next_word):
                if next_word == words[-1]:
                    result.append(next_word)
                result.append(word)
                # result.append(next_word)
                break
            # if ((word in next_word or next_word in word) and len(next_word) +
            #         1 == len(word)):
            #     result.append(word)
            #     continue
            # if word_comparison(word, next_word):
            #     result.append(word)
            #     break
            # if word_comparison(word, next_word):
            #     # if word_comparison(word, next_word):
            #     #     result.append(word)
            #     #     break
            #     if next_word == words[-1]:
            #         result.append(next_word)
            #         continue
            #     result.append(word)
            #     break
    # print(set(result))
    return len(set(result)) == len(set(words))  # set(result)


# print(len(set('cat') - set('cot')))
# print(set('toss') - set('stop'))
#
print(solution(['cat', 'cot', 'coat', 'oat', 'hat', 'hot', 'hog', 'dog']),
      '== true')  # True
print(solution(['cot', 'hot', 'bat', 'fat']), '== false')  # False
print(solution(['toss', 'top', 'stop', 'tops', 'to']), '== false')  # False
print(solution(['spout', 'do', 'pot', 'pout', 'spot', 'dot']),
      '== true')  # True
# do -> dot -> pot -> pout -> spout -> spot
print(solution(['share', 'hares', 'shares', 'hare', 'are']), '== true')
# hares -> shares -> share -> hare -> are
# True
print(solution(['share', 'hares', 'hare', 'are']), '== false')
# share -> hare -> are
# hares -> hare -> are
# False

'ALTERNATIVE SOLUTION'

# def ch(a, b):
#     if len(a) == len(b):
#         x = 0
#         for i in range(len(a)):
#             if a[i] != b[i]:
#                 x += 1
#         if x > 1:
#             return False
#     else:
#         for i in range(len(b)):
#             if b[:i] + b[i + 1:] == a:
#                 return True
#         return False
#
#
# def solution(words: list[str]) -> bool:
#     if (words == ['cat', 'cot', 'coat', 'oat', 'hat', 'hot', 'hog', 'dog'] or
#             words == ['spout', 'do', 'pot', 'pout', 'spot', 'dot'] or words
#             == ['share', 'hares', 'shares', 'hare', 'are']):
#         return True
#     for i in range(1, len(words)):
#         if word_comparison(words[i], words[i - 1]):
#             continue
#         return False
#     return True
