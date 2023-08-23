"""В этой практике вы будете реализовывать функции для работы с множествами,
как с наборами флагов.

Флаги помогают управлять работой некоторого кода: если флаг поднят, значит
какая-то возможность включена. В этом плане флаги похожи на галочки в формах и
бланках — галочку тоже можно поставить или не поставить.

В нашем случае флаги будут представлять собой элементы множества: если элемент
в множестве присутствует, значит и флаг поднят. Вам же нужно будет реализовать
две функции: toggle() и toggled().

Функция toggle()
Эта функция должна принимать в качестве аргументов:
- один флаг
- множество

Если флаг уже присутствует в множестве, его нужно убрать. Если же флаг
отсутствует, то его нужно добавить. Таким образом функция будет переключать
состояние флага. Множество нужно заменять по месту, возвращать из функции
ничего не нужно."""

"""Посмотрим на пример использования функции toggle():"""

# READ_ONLY = 'read_only'
# flags = set()
# toggle(READ_ONLY, flags)
# READ_ONLY in flags  # True
# toggle(READ_ONLY, flags)
# READ_ONLY in flags  # False

"""Функция toggled()
Эта функция работает похожим на toggle() образом. Вместо изменения исходного
множества эта функция возвращает новое множество — с уже переключенным флагом.
Посмотрим на примере:"""

# READ_ONLY = 'read_only'
# flags = set()
# new_flags = toggled(READ_ONLY, flags)
# READ_ONLY in flags  # False
# READ_ONLY in new_flags  # True


def toggle(flag, flag_set):
    if flag not in flag_set:
        flag_set.add(flag)
    elif flag in flag_set:
        flag_set.discard(flag)


READ_ONLY = 'read_only'
flags = set()
toggle(READ_ONLY, flags)
print(READ_ONLY in flags)  # True
toggle(READ_ONLY, flags)
print(READ_ONLY in flags)  # False


def toggled(flag, flag_set):
    new_flag_set = flag_set.copy()
    if flag not in new_flag_set:
        new_flag_set.add(flag)
    elif flag in new_flag_set:
        new_flag_set.discard(flag)
    return new_flag_set


READ_ONLY = 'read_only'
flags = set()
new_flags = toggled(READ_ONLY, flags)
print(READ_ONLY in flags)  # False
print(READ_ONLY in new_flags)  # True


# def toggle(flag, flag_set):  ---> solution
#     if flag in flag_set:
#         flag_set.discard(flag)
#     else:
#         flag_set.add(flag)


# def toggled(flag, flag_set):
#     new_set = flag_set.copy()
#     toggle(flag, new_set)
#     return new_set
