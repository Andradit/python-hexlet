import math

"""В этой задаче тесты написаны для отрезков, которые используют точки. Ваша
задача — реализовать интерфейсные функции для работы с точками. Внутреннее
представление точек должно быть основано на полярной системе координат,
хотя интерфейс предполагает работу с декартовой системой (снаружи).

Реализуйте интерфейсные функции точек:

    - make_point() — принимает на вход координаты и возвращает точку,
    уже реализован;
    - get_x()
    - get_y()
"""

# x = 4
# y = 8

# point хранит в себе данные в полярной системе координат
# point = make_point(x, y)

# Здесь происходит преобразование из полярной в декартову
# get_x(point)  # 4
# get_y(point)  # 8

"""Подсказки
    - трансляция декартовых координат в полярные была описана в теории
    - получить x можно по формуле radius * cos(angle);
    - получить y можно по формуле radius * sin(angle)
"""



def make_point(x, y):
    return {
        "angle": math.atan2(y, x),
        "radius": math.sqrt((x ** 2) + (y ** 2)),
    }

x = 4
y = 8

point = make_point(x, y)
print(point)


def get_x(point):
    radius = point["radius"]
    angle = point["angle"]
    return radius * math.cos(angle)

def get_y(point):
    radius = point["radius"]
    angle = point["angle"]
    return radius * math.sin(angle)

print(get_x(point))
print(get_y(point))