"""В этом упражнении вам предстоит анализировать изменения в старой и новой
версии словаря. Вам нужно реализовать функцию diff_keys(), которая должна:

Принимать два словаря-аргумента — старый и новый
Возвращать словарь с результатами анализа
Результирующий словарь должен содержать строго три ниже перечисленных ключа:

'kept' — множество ключей, которые присутствовали в старом словаре и остались
в новом
'added' — множество ключей, которые отсутствовали в старом словаре, но
появились в новом
'removed' — множество ключей, которые присутствовали в старом словаре, но в
новый не вошли
Обратите внимание, что в этом упражнении сравниваются только ключи, а не
значения."""


def diff_keys(old_dict, new_dict):
    result_dict = {}
    old_keys = set(old_dict.keys())
    new_keys = set(new_dict.keys())

    result_dict['kept'] = old_keys & new_keys
    result_dict['added'] = new_keys - old_keys
    result_dict['removed'] = old_keys - new_keys

    return result_dict


# def diff_keys(old, new):  ---> solution
#     old_keys = set(old)
#     new_keys = set(new)
#     return {
#         'kept': old_keys & new_keys,
#         'added': new_keys - old_keys,
#         'removed': old_keys - new_keys,
#     }

print(diff_keys({'name': 'Bob', 'age': 42}, {}))
# # {'kept': set(), 'added': set(), 'removed': {'name', 'age'}}
print(diff_keys({}, {'name': 'Bob', 'age': 42}))
# # {'kept': set(), 'added': {'name', 'age'}, 'removed': set()}
print(diff_keys({'a': 2}, {'a': 1}))
# # {'kept': {'a'}, 'added': set(), 'removed': set()}""
