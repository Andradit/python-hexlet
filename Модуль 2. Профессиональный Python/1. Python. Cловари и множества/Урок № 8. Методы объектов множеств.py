'''Цель упражнения — написать функцию apply_diff().

Эта функция принимает два аргумента:

Множество, которое нужно будет изменять по месту (возвращать ничего не нужно)
Словарь, который может содержать ключи 'add' и 'remove' с множествами в
качестве значений.
Значения по ключу 'add' нужно добавить в изменяемое множество, а значения по
ключу 'remove' — убрать из множества. Прочие ключи в переданном словаре
значения не имеют и обрабатываться не должны.

target = {'a', 'b'}
diff = {'add': {'c'}, 'remove': {'a'}}
apply_diff(target, diff)
print(target)  # => {'c', 'b'}

Подсказки
В этом упражнении нужно манипулировать множествами целиком, поэтому не нужно
использовать методы add и discard'''


def apply_diff(set, dict):
    for k in dict.keys():
        if k == 'add':
            set.update(dict[k])
        if k == 'remove':
            set.difference_update(dict[k])


target = {'a', 'b'}
diff = {'add': {'c'}, 'remove': {'a'}}
apply_diff(target, diff)
print(target)  # => {'c', 'b'}

# SOLUTION
# def apply_diff(set_for_update, diff):
#     set_for_update.update(diff.get('add', {}))
#     set_for_update.difference_update(diff.get('remove', {}))
