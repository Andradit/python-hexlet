'''Создайте словарь из строки 'pythonist' следующим образом: в качестве ключей
возьмите буквы строки, а значениями пусть будут числа, соответствующие
количеству вхождений данной буквы в строку.'''

string = 'pythonist'
dict = {}
for k in string:
    if k in dict:
        dict[k] = dict[k] + 1
    else:
        dict[k] = 1
print(dict)

# SOLUTION:
'''Для решения данной задачи воспользуемся функцией count(), которая считает
количество вхождений элемента в строку. Для генерации словаря воспользуемся
синтаксисом представления словарей (dictionary comprehention).'''

str1 = 'pythonist'
my_dict = {i: str1.count(i) for i in str1}
print(my_dict)
