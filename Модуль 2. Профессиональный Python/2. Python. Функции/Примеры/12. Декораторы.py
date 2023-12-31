"""В программировании часто возникают задачи, когда нужно добавить поведение
к уже существующим функциям или классам. Например, логирование, проверку
входных данных или замер времени выполнения функции. В таких случаях
использование декораторов может значительно упростить решение задачи.

В этом уроке мы рассмотрим, что такое декораторы и как их использовать,
чтобы добавлять дополнительную функциональность к существующим функциям.
--------------------------------------------------------------------------------
Что такое декораторы
--------------------------------------------------------------------------------
Декораторы позволяют динамически изменять поведение
функций и классов с помощью добавления или изменения их функциональности без
изменения самого кода.

Декораторы в Python — это функции, которые принимают другую функцию в
качестве аргумента, добавляют к ней некоторую дополнительную функциональность
и возвращают функцию с измененным поведением.

Декораторы используются, чтобы изменять работу существующих функций или
классов, добавлять новые возможности и обеспечивать безопасность.

Предположим, что у нас есть функция, которая выполняет математические
операции и возвращает результат:"""


def add_numbers(x, y):
    return x + y


"""Мы можем создать декоратор, который добавит к этой функции 
функциональность для отладки:"""


def debug_decorator(func):
    def wrapper(*args, **kwargs):
        print("Вызов функции:", func.__name__)
        print("Аргументы:", args, kwargs)
        result = func(*args, **kwargs)
        print("Результат:", result)
        return result

    return wrapper


"""Этот декоратор принимает функцию в качестве аргумента и возвращает новую 
функцию-обертку, которая добавляет отладочные сообщения в процесс выполнения 
исходной функции. Чтобы применить этот декоратор к функции add_numbers, 
мы можем вызвать эту функцию с аргументом:"""


@debug_decorator
def add_numbers(x, y):
    return x + y


"""Теперь функция add_numbers будет выполняться с дополнительными отладочными 
сообщениями:"""

add_numbers(2, 3)
# Вызов функции: add_numbers
# Аргументы: (2, 3) {}
# Результат: 5

"""Также мы можем создавать несколько декораторов для одной функции, которые 
будут применяться последовательно:"""


@debug_decorator
@time_decorator
def add_numbers(x, y):
    return x + y


"""В этом примере сначала применится декоратор времени выполнения, а затем 
отладочный декоратор.
--------------------------------------------------------------------------------
Как связаны декораторы и замыкания
--------------------------------------------------------------------------------
Внутренняя функция wrapper декоратора 
обычно ссылается на переменные из внешней функции, что создает замыкание. В 
примере с декоратором debug_decorator функция wrapper ссылается на func, 
которая была определена во внешней функции debug_decorator. Это позволяет 
декоратору использовать и изменять переменные из внешней функции в рамках 
своей логики работы, что делает декораторы более гибкими инструментами.

Также декораторы могут использовать замыкания, чтобы сохранять состояния 
между вызовами функции. Например, декоратор может создать замыкание, которое 
сохраняет информацию о том, сколько раз функция была вызвана, и возвращать 
это значение при каждом вызове функции.

Вот пример декоратора, который использует замыкание, чтобы отслеживать 
количество вызовов функции:"""


def count_calls(func):
    num_calls = 0

    def wrapper(*args, **kwargs):
        nonlocal num_calls
        num_calls += 1
        print(f"Функция была вызвана {num_calls} раз(а)")
        return func(*args, **kwargs)

    return wrapper


@count_calls
def my_func():
    print("Hello, world!")


my_func()
# Функция была вызвана 1 раз(а)
# Hello, world!
my_func()
# Функция была вызвана 2 раз(а)
# Hello, world!

"""В этом примере декоратор count_calls принимает функцию func и возвращает 
новую функцию wrapper. Последняя отслеживает количество вызовов func и 
выводит сообщение при каждом вызове. Затем декоратор применяется к функции 
my_func. Каждый раз, когда my_func вызывается, декоратор увеличивает счетчик 
вызовов и выводит сообщение.

Рассмотрим еще один пример, где создадим декоратор, который измеряет время 
выполнения функции:"""

import time


def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(
            f"Время выполнения функции {func.__name__}: {end_time - start_time}"
            f"сек."
        )
        return result

    return wrapper


@timer
def some_function():
    time.sleep(2)


some_function()
# Время выполнения функции some_function: 2.000108242034912 сек.

"""Здесь мы определяем декоратор timer, который принимает функцию func и 
возвращает функцию-обертку wrapper. Функция-обертка вызывает функцию func, 
замеряет время ее выполнения и сохраняет результат работы func в переменную 
result. Затем функция-обертка выводит время выполнения функции на экран и 
возвращает результат вызова функции.

В конце применяем декоратор timer к функции some_function. Когда мы вызываем 
функцию some_function, декоратор автоматически вызывается и выводит время 
выполнения функции на экран.
--------------------------------------------------------------------------------
Выводы
--------------------------------------------------------------------------------
Существует большое количество готовых декораторов, доступных в 
стандартной библиотеке Python и других библиотеках. Некоторые из них 
позволяют кэшировать результаты функций, обеспечивать авторизацию и 
безопасность, профилировать код, проверять типы данных и многое другое.

Декораторы могут повлиять на производительность кода, поэтому их следует 
использовать с умом и осторожностью. Также нужно учитывать, что декораторы 
могут усложнить отладку кода и сделать его менее понятным для других 
разработчиков.

При этом декораторы являются мощным инструментом, который позволяет легко 
добавлять дополнительную функциональность к существующим функциям и классам и 
не изменять их исходный код. Также использование замыканий позволяет 
декораторам сохранять состояние между вызовами функций. Это делает их еще 
более мощными инструментами программирования на Python."""
