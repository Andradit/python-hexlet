"""Вам предстоит реализовать два решения одной и той же задачи —
функциональное и процедурное.

Задача состоит в том, чтобы для входного списка списков получить список
нечетных чисел по порядку списков (первый, третий и так далее), оставив в
каждом списке только нечетные по порядку элементы.

Например, из списка [[1, 2, 3], [4, 5, 6], [7, 8, 9]] должен получиться
список [[1, 3], [7, 9]].

Функциональное решение должно вычислять новый список списков на основе
оригинального. Оригинальный список должен оставаться неизменным. У вас должна
получиться функция odds_from_odds():"""

# from solution import odds_from_odds

# l = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# odds_from_odds(l)
# # [[1, 3], [7, 9]]
# print(l)  # Оригинал не изменился
# # => [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# odds_from_odds([])  # Пустой список не должен быть проблемой
# # []
# odds_from_odds([[]])  # Как и список пустых списков
# # [[]]

'''Процедурное решение должно изменить список-аргумент по месту, 
а не возвращать его новую версию. Постарайтесь обойтись без создания 
вспомогательных структур, в том числе для обработки вложенных списков. У вас 
должна получиться функция keep_odds_from_odds():'''


# from solution import keep_odds_from_odds

# l = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# keep_odds_from_odds(l)  # Процедура ничего не возвращает
# print(l)  # Но при этом она меняет аргумент
# # => [[1, 3], [7, 9]]
# keep_odds_from_odds(l)
# print(l)
# # => [[1]]
# keep_odds_from_odds(l)
# print(l)  # Тут уже ничего четного не осталось, поэтому изменений нет
# # => [[1]]
# keep_odds_from_odds([])  # Пустой список не должен быть проблемой
# keep_odds_from_odds([[]])  # Как и список пустых списков

def odds_from_odds(list_of_lists):
    res_list = []
    for index, value in enumerate(list_of_lists):
        if index % 2 == 0:
            if isinstance(value, list):
                res_list.append(odds_from_odds(value))
            else:
                res_list.append(value)
    return res_list


def keep_odds_from_odds(list_of_lists):
    index = 0
    for i in range(len(list_of_lists)):
        if i % 2 == 0:

            if isinstance(list_of_lists[index], list):
                keep_odds_from_odds(list_of_lists[index])
        else:
            index += 1
            list_of_lists.pop(index)

    return list_of_lists


l = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(odds_from_odds(l))
print(keep_odds_from_odds(l))  # [[1, 3], [7, 9]]
# print(l)  # Оригинал не изменился => [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print(odds_from_odds([]))  # []
# print(odds_from_odds([[]]))  # [[]]

"SOLUTION"

# def odds(source):
#     is_odd_position = lambda pair: pair[0] % 2 == 0  # noqa: E731
#     get_value = lambda pair: pair[1]  # noqa: E731
#     return list(map(
#         get_value,
#         (filter(is_odd_position, enumerate(source)))
#     ))


# def odds_from_odds(list_of_lists):
#     return list(map(odds, odds(list_of_lists)))

"""# Альтернативное решение с помощью itemgetter
# https://docs.python.org/3/library/operator.html#operator.itemgetter
#
# odds = itemgetter(slice(None, None, 2))
#
# def odds_from_odds(list_of_lists):
#     return list(map(odds, odds(list_of_lists)))"""


# def keep_odd(some_list):
#     index = 0
#     for i in range(len(some_list)):
#         if i % 2 == 1:
#             some_list.pop(index)
#         else:
#             index += 1
#
#
# def keep_odds_from_odds(list_of_lists):
#     keep_odd(list_of_lists)
#     for one_list in list_of_lists:
#         keep_odd(one_list)