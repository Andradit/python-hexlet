'''Вам предстоит реализовать пару функций:

Функцию-ключ get_first_name(), которая получает имя пользователя из строки
вида "Имя_Фамилия"'''

# get_first_name("Vader_Darth")  # Vader

'''Функцию сортировки sort_by(), которая принимает функцию-ключ и список и
сортирует список по этому ключу. Функция не должна изменять оригинальный
список.'''
# users = ["Vader_Darth", "Luke_Skywalker", "Boba_Fett"]

# sort_by(get_first_name, users)  # ["Boba_Fett", "Luke_Skywalker",
# "Vader_Darth"]
# print(users) # => ["Vader_Darth", "Luke_Skywalker", "Boba_Fett"]

'''Подсказки.
Для сортировки используйте встроенную функцию sorted()'''


def get_first_name(user_name):
    result, _ = user_name.split('_', 1)
    return result


# print(get_first_name("Vader_Darth"))  # Vader


def sort_by(function, item):
    return sorted(item, key=function)


users = ["Vader_Darth", "Luke_Skywalker", "Boba_Fett"]

print(sort_by(get_first_name, users))
# ["Boba_Fett", "Luke_Skywalker", # "Vader_Darth"]

print(users)  # ["Vader_Darth", "Luke_Skywalker", "Boba_Fett"]


# SOLUTION
# def get_first_name(fullname):
#     return fullname.split('_')[0]


# def sort_by(key, coll):
#     return sorted(coll, key=key)
