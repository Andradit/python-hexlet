'''Переменное количество аргументов.

Функция print принимает то количество аргументов, которые ей передаётся. Она
даже работает, когда ее вызывают без аргументов.

Рассмотрим пример функции с неограниченным количеством аргументов:'''


def f(*args):
    print(type(args))
    print(args)


print(f())
# => tuple
# => ()

print(f(1, 'a', None, False))
# => tuple
# => (1, 'a', None, False)

'''Эта функция отличается от функции с позиционными аргументами аргументом
*args. Точнее оператором *. Он упаковывает все передаваемые в функцию
аргументы от текущей позиции и до конца в переменную как кортеж.

Аргумент с оператором * забирает в себя все переданные значения. Если
необходимо использовать дополнительные аргументы, их нужно указать перед
аргументом с оператором *, как показано в примере:'''


def f(x, *args):
    print(f'Первый аргумент: {x}')
    for a in args:
        print(f'Другой аргумент из *args {a}!')


f('Programing language', 'Python', 'PHP', 'Java')
# => Первый аргумент: Programing language
# => Другой аргумент из *args Python!
# => Другой аргумент из *args PHP!
# => Другой аргумент из *args Java!

f()
# TypeError: f() missing 1 required positional argument: 'x'
'''Здесь функция принимает несколько аргументов, но как минимум один должен
быть передан всегда. Первый аргумент станет значением переменной x, а
остальные сохранятся в *args. Так можно делать любое нужное количество
обязательных аргументов.'''

'''Передача аргументов в форме коллекции'''

'''Иногда нужно сначала сформировать набор аргументов, а потом передать их
функции. Допустим, прочитать аргументы из файла или получить другим
программным способом. Здесь снова пригодится оператор *:'''


def sum(a, b):
    return a + b


nums = [3, 4]
print(sum(*nums))  # 7

'''Часть аргументов можно подставлять сразу в функцию и даже подставлять
несколько коллекций сразу:'''


def greet(*names):
    for name in names:
        print(f'Hello, {name}!')


greet(
   'Bob', *['Mary', 'Clair'], 'Sam',
   *('Henry', 'John')
)
# => Hello, Bob!
# => Hello, Mary!
# => Hello, Clair!
# => Hello, Sam!
# => Hello, Henry!
# => Hello, John!
'''В приведенном примере был передан в функцию greet набор аргументов и
коллекций. При помощи оператора * функция greet вызывается с шестью
аргументами: 'Bob', 'Mary', 'Clair', 'Sam', 'Henry' и 'John'. Результатом
этого кода будет шесть приветствий по одному для каждого аргумента. Они будут
в том порядке, в котором их передали в функцию.'''
