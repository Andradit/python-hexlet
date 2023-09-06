'''Создайте словарь с количеством элементов не менее 5-ти. Поменяйте местами
первый и последний элемент объекта. Удалите второй элемент. Добавьте в конец
ключ «new_key» со значением «new_value». Выведите на печать итоговый словарь.
Важно, чтобы словарь остался тем же (имел тот же адрес в памяти).'''
from collections import OrderedDict


dictionary = {
             'a': 1,
             'b': 2,
             'c': 3,
             'd': 4,
             'e': 5
                    }

print(id(dictionary))

dict = OrderedDict(dictionary)
first_element = list(dict.items())[0]
print(first_element)
dict.move_to_end(key=first_element[0])
print(dict)
last_element = list(dict.items())[-2]
print(last_element)
dict.move_to_end(key=last_element[0], last=False)
print(dict)

second_element = list(dict.items())[1]
del dict[second_element[0]]
print(dict)


dict['new_key'] = 'new_value'
dictionary.clear()
dictionary.update(dict)
print(dictionary)

print(id(dictionary))
