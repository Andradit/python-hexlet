"""Напишите тесты для функции get(collection, key, default_value). Эта
функция извлекает значение из словаря при условии, что ключ существует. В
ином случае возвращается default_value:"""

# from functions import get_function
# get = get_function()
#
# get({"hello": "world"}, "hello")  # world
# get({"hello": "world"}, "hello", "kitty")  # world
# get({}, "hello", "kitty")  # kitty

"""Тесты должны быть построены по такому же принципу, как это описывалось в 
теории урока: проверка через if и исключение в случае провала теста.

Для хорошего тестирования этой функции понадобится как минимум три теста. 
Нужно проверить:

    1. Возвращает ли функция нужное значение по существующему ключу (прямой 
    тест на работоспособность).
    2. Возвращается ли значение по умолчанию, если ключа нет.
    3. Возвращается ли значение по существующему ключу, даже если передано 
    значение по умолчанию (тест пограничного случая)"""

from functions import get_function

get = get_function()

if get({"key": "value"}, "key") != 'value':
    raise Exception('FAILED!')

if get({"key": "value"}, "key", "default_value") != 'value':
    raise Exception('FAILED!')

if get({}, "key", "default_value") != 'default_value':
    raise Exception('FAILED!')
