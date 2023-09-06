'''Даны два словаря:
dictionary_1 = {'a': 300, 'b': 400} и
dictionary_2 = {'c': 500, 'd': 600}.
Объедините их в один при помощи встроенных функций языка Python.
'''


def merged(dict_1, dict_2):
    dict = {}
    for k in dict_1.keys():
        if k not in dict:
            dict[k] = [dict_1[k]]
        else:
            dict[k].append(dict_1[k])
    for k in dict_2.keys():
        if k not in dict:
            dict[k] = [dict_2[k]]
        else:
            dict[k].append(dict_2[k])
    return dict


dictionary_1 = {'a': 300, 'b': 400, 'c': 800}
dictionary_2 = {'c': 500, 'd': 600}

print(merged(dictionary_1, dictionary_2))


# SOLUTION:
'''Для объединения двух словарей создадим третий словарь в виде копии первого.
Для этого используем встроенную функцию copy(). Далее к уже созданному словарю
мы присоединяем второй словарь. Для этого мы используем встроенную функцию
update().'''

# dictionary_1 = {'a': 100, 'b': 200}
# dictionary_2 = {'x': 300, 'y': 200}
# dictionary_3 = dictionary_1.copy()
# dictionary_3.update(dictionary_2)
# print(dictionary_3)
