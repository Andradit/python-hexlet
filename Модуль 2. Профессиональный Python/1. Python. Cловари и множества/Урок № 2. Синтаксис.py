"""В этой практике вам нужно реализовать две функции:

Функцию make_user(), которая должна принимать два параметра — имя пользователя
и возраст. Функция должна вернуть словарь с ключами 'name' и 'age', по которым
должны быть сохранены соответствующие значения
Функцию format_user(), которая принимает словарь — результат вызова функции
make_user(). Она должна вернуть строку вида 'Phil, 25'

phil = make_user('Phil', 25)
type(phil)
# <class 'dict'>
format_user(phil)
# Phil, 25"""


def make_user(name_user, age_user):
    dictionary = {}
    dictionary['name'] = name_user
    dictionary['age'] = age_user
    return dictionary


def format_user(user):
    return f'{user["name"]}, {user["age"]}'


bob = make_user('Bob', 33)
print(bob)
print(format_user(bob))
