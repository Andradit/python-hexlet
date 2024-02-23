"""Вам предстоит написать функцию non_empty_truths(). Она должна вычислять
копию входного списка списков с помощью генераторов списков. При этом копия
должна быть очищена от всего лишнего:

- от ложных элементов — не только False, а любых ложных;
- от пустых списков — они могут появиться сами по себе или получаться после
отбрасывания всех элементов из них.

Использование полученной функции должно выглядеть так:"""

# non_empty_truths([])  # Нечего отбрасывать, это тоже нормально
# # []
# non_empty_truths([[], []])  # Отбрасываем пустые списки
# # []
# non_empty_truths([[0]])  # Чистые, но пустые списки тоже отбрасываем
# # []
# non_empty_truths([[0, ""], [False, None]])  # В Python многое считается ложным
# # []
# non_empty_truths([[0, 1, 2], [], [], [False, True, 42]])
# # [[1, 2], [True, 42]]

"""Подсказки:

- генераторы списков могут быть вложенными прямо вместе с квадратными скобками:
[.. for ... in [... for ... in ...] ...]. Считайте это промежуточными списками
для вложенных циклов;
- выражением, вычисляющимся в элемент генератора списков может быть и список: 
[[..] for ...]. Так вы получите список списков;
- сами по себе пустые списки — тоже ложные"""


def non_empty_truths(list_of_lists):
    # for x in list_of_lists:
    #     if x:
    #         for y in x:
    #             if y:
    #                 return y
    #     return x
    return [
        true_elem
        for true_elem in [[elem for elem in inner_list if elem]
                          for inner_list in list_of_lists] if true_elem
    ]


"SOLUTION"


# def non_empty_truths(list_of_lists):
#     return [
#         truths for truths in
#         [[elem for elem in one_list if elem]  # noqa: WPS335
#          for one_list in list_of_lists
#          ]
#         if truths
#     ]


print(non_empty_truths([]))  # []
print(non_empty_truths([[], []]))  # []
print(non_empty_truths([[0]]))  # []
print(non_empty_truths([[0, ""], [False, None]]))  # []
print(non_empty_truths([[0, 1, 2], [], [], [False, True, 42]]))
# [[1, 2], [True, 42]]
print(non_empty_truths([[], [1], [], [2]]))  # [[1], [2]]

lists = [[1, 2, 3, 5], [7, 11, 8, 0], [21, 12, 2, 7, 1], [1, 3]]
print([x for x in [[elem for elem in one_list if elem % 2 == 1] for one_list in
                   lists] if len(x) >= 3])
