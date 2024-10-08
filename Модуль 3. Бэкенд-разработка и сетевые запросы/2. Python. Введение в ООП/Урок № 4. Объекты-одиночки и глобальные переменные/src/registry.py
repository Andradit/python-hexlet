CLASSES = {}


def add(clazz):
    # слово clazz часто используется, чтобы называть переменную, которая
    # ссылается на некий класс. Оригинальное слово "class" в качестве переменной
    # использовать нельзя, потому что в языке уже есть такое ключевое слово.
    # атрибут `clazz.__module__` хранит строку с именем модуля,
    # в котором класс был (изначально) объявлен
    # атрибут `clazz.__name__` хранит строку с именем класса
    key = f'{clazz.__module__}.{clazz.__name__}'
    CLASSES[key] = clazz
