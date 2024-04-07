"""Отрезок — еще один графический примитив. В коде описывается парой точек,
одна из которых — начало отрезка, другая — конец. Обычный отрезок не имеет
направления, поэтому вы сами можете выбирать, какую точку считать началом,
а какую концом.

В этом задании подразумевается, что вы уже понимаете принцип построения
абстракции. Вы способны самостоятельно принять решение о том, как она будет
реализована. Сделать это можно разными способами и нет одного правильного.

Реализуйте указанные ниже функции:

    make_segment() — принимает на вход две точки и возвращает отрезок;
    get_mid_point_of_segment() — принимает на вход отрезок и возвращает точку,
    которая находится на середине отрезка;
    get_begin_point() — принимает на вход отрезок и возвращает точку начала;
    отрезка get_end_point() — принимает на вход отрезок и возвращает точку конца
    отрезка.

Представление отрезка вы должны придумать сами.

Пример работы:"""

# segment = make_segment(make_decart_point(3, 2), make_decart_point(0, 0))
# # В примерах ниже возвращаются точки с координатами (x, y)
# get_begin_point(segment)  # {'x': 3, 'y': 2}
# get_end_point(segment)  # {'x': 0, 'y': 0}
# get_mid_point_of_segment(segment)  # {'x': 1.5, 'y': 1}

"""Подсказки

Для создания точек используйте функцию make_decart_point()"""


'IMPORT in SOLUTION'
def make_decart_point(x, y):
    return {"x": x, "y": y}


def get_x(point):
    return point["x"]


def get_y(point):
    return point["y"]


def make_segment(point_1, point_2):
    segment = {
        "begin_point": point_1,
        "end_point": point_2,
    }
    return segment


def get_begin_point(segment):
    return segment["begin_point"]


def get_end_point(segment):
    return segment["end_point"]


def get_mid_point_of_segment(segment):
    begin_point = get_begin_point(segment)
    end_point = get_end_point(segment)
    x = (get_x(begin_point) + get_x(end_point)) / 2
    y = (get_y(begin_point) + get_y(end_point)) / 2
    return make_decart_point(x, y)


segment = make_segment(make_decart_point(3, 2), make_decart_point(0, 0))
# print(segment)
# В примерах ниже возвращаются точки с координатами (x, y)
print(get_begin_point(segment))  # {'x': 3, 'y': 2}
print(get_end_point(segment))  # {'x': 0, 'y': 0}
print(get_mid_point_of_segment(segment))  # {'x': 1.5, 'y': 1}
