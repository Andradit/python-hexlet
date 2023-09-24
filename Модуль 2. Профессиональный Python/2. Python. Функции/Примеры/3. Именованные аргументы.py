'''В Python у функций могут быть еще и именованные аргументы — keyword
arguments.

Например, мы вызываем следующую функцию:'''


def bar(length, char1, char2):
    return (char1 + char2) * length + char1


print(bar(5, '-', '*'))  # => -*-*-*-*-*-

'''У функции bar три аргумента. При вызове функции с позиционными аргументами
важную роль играет порядок размещения передаваемых аргументов. Но если мы
хотим изменить порядок, то нужно использовать именованные аргументы. В этом
уроке мы научимся работать с ними.'''

'''Именованные аргументы.

Чтобы передать именованные аргументы в функцию, нужно указать их имена,
которые были заданы при объявлении функции:
'''


def bar(length, char1, char2):
    return (char1 + char2) * length + char1


print(bar(length=3, char1='-', char2='*'))  # => -*-*-*-
print(bar(char1='-', char2='*', length=3))  # => -*-*-*-
print(bar(char2='*', length=3, char1='-'))  # => -*-*-*-

'''При вызове функции меняется порядок передаваемых аргументов. Когда функции
назначаются соответствующие значения именованных аргументов, Python учитывает
их имена, а не позиции. В результате функция будет всегда выводить одно и то
же значение независимо от позиций переданных ей аргументов.
'''
'''Значения аргументов по умолчанию.

Предположим, что char1 и char2 чаще получают одни и те же значения. В такой
ситуации удобно указать значения по умолчанию:'''


def bar(length, char1='-', char2='*'):
    return (char1 + char2) * length + char1


print(bar(5))  # => -*-*-*-*-*-
print(bar(3, '.'))  # => .*.*.*.
print(bar(2, ':', '|'))  # => :|:|:

'''Теперь предположим, что нас устраивает значение по умолчанию для char1, но
мы хотим задать свое значение для char2. Это можно сделать с помощью
именованных аргументов:
'''
print(bar(4, char2='#'))
# => -#-#-#-#-
print(bar(char2='$', length=3))
# => -$-$-$-

'''Здесь имеет значение порядок групп аргументов — позиционные значения должны
быть указаны до именованных. Иначе мы получим ошибку:'''

# print(bar(char2='%', 2))
# => SyntaxError: positional argument follows keyword argument

'''Если у функции есть позиционные аргументы без значений по умолчанию,
значения для этих аргументов все равно нужно указать либо в виде позиционных
значений, либо в виде именованных. Нарушение этого правила приведет к ошибке
вида:'''

bar(char2='!')
# TypeError: bar() missing 1 required positional argument: 'length'

'''Нужно различать синтаксис объявления аргументов функции и синтаксис вызова
функции. При вызове функции у нас больше свободы. Например, можно указывать
именованные аргументы перед разворачиваемой группой позиционных:'''


def f(*args, x=None, y=None):
    print('args =', args, ', x =', x, ', y =', y)


f(*(1, 2), x='a', *[3, 4], y='b', *(5, 6))
# => args = (1, 2, 3, 4, 5, 6), x = a, y = b

'''В данном примере переменная args содержит все позиционные аргументы,
которые были переданы функции. А переменные x и y содержат значения
аргументов, которые были переданы по именам.'''

'''Случаи применения именованных аргументов.

Нет строгих правил, по которым используются именованные аргументы. Однако
широко практикуется такой подход: если функция принимает больше трех
аргументов, нужно хотя бы часть из них указать по имени. Важно именовать
значения аргументов, если несколько значений имеют одинаковый тип. В другом
случае будет трудно понять, что делает функция с подобным вызовом:'''

# make('circle', 300, 150, 10, None, 2.5, False)

'''Сравним с этим:'''

# make(
#     shape='circle',
#     x=300, y=150, radius=10,
#     line_pattern=None,
#     line_width=2.5,
#     fill=False
# )
'''Такой код читать проще.

У вышеупомянутого правила есть пара исключений:

- если по названию функции можно сразу понять, что она выполняет и какие
параметры принимает, то имена аргументам не задаются. Например, можно понять,
что скрывается за значениями в вызове point3d(10, 50, 21) или rgb(0, 255, 0)
- не нужно указывать имена аргументам, которые объявлены через *. У этого нет
смысла и возможности'''

# def sum(*args):
#   …

# sum(x1=1, x2=2) => TypeError: sum() got an unexpected keyword argument 'x1'

'''В таких функциях имя args недоступно извне, ведь это не один аргумент, а
получатель произвольного их количества.'''
