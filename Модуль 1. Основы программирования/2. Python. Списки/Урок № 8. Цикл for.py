# for x in [0, 1, 2]:
#    if x:
#        break
# else:
#    x = 0

# print(x)


"""В этом упражнении вы будете реализовывать классический цикл поиска. Функция find_index(), которую вам предстоит написать, должна принимать значение и нечто, по чему можно итерироваться — строку, список, кортеж. В ответ функция должна вернуть индекс первого элемента итерируемой последовательности, равного заданному значению. Если же значение в последовательности не встречается или же последовательность окажется пустой, функция должна вернуть None.

find_index('t', 'cat')  # 2
find_index(5, [1, 2, 3, 4, 5, 6, 7])  # 4
find_index(42, []) is None  # True
find_index('!', 'abc') is None  # True

Подсказки
При выполнении воспользуйтесь циклом for и функцией enumerate()."""


def find_index(value, items):
    for (index, _) in enumerate(items):
        if value == items[index]:
            return index


print(find_index('t', 'cat'))  # 2
print(find_index(5, [1, 2, 3, 4, 5, 6, 7]))  # 4
print(find_index(42, []) is None)  # True
print(find_index('!', 'abc') is None)  # True
