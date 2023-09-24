'''Вам нужно реализовать функцию greet(), которая должна принимать несколько
имён (как минимум одно!) и возвращать строку приветствия (см. примеры ниже).'''

# greet('Bob') ---> 'Hello, Bob!'
# greet('Moe', 'Mary') ---> 'Hello, Moe and Mary!'
# greet(*'ABC') ---> 'Hello, A and B and C!'

'''Подсказки
При решении вам может пригодиться метод join() у объекта строки. Работает он
так:'''
# ','.join(['A', 'B', 'C']) ---> 'A,B,C'
# ','.join(['A']) ---> 'A'
# ''.join(['Hello', 'World']) ---> 'HelloWorld'


def greet(name, *args):
    names = ' and '.join((name,) + args)
    return f'Hello, {names}!'


greet('Bob')
greet('Moe', 'Mary')
greet(*'ABC')

greet('Bob')
greet('Bob', 'Ann')
greet('Bob', 'Ann', 'Moe')


# SOLUTION
# def greet(who, *args):
#     names = ' and '.join((who,) + args)
#     return f'Hello, {names}!'
