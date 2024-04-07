"""Реализуйте функцию, которая находит точку посередине между двумя
указанными точками:

Пример работы:"""

# point1 = {'x': 0, 'y': 0}
# point2 = {'x': 4, 'y': 4}
# get_mid_point(point1, point2)  # {'x': 2, 'y': 2}

"""Подсказки

Средняя точка вычисляется по формуле x = (x1 + x2) / 2 и y = (y1 + y2) / 2."""


def get_mid_point(point_1, point_2):
    res_dict = {}
    for key in point1.keys():
        res_dict[key] = (point_1[key] + point_2[key]) / 2
    return res_dict


'SOLUTION'
# def get_mid_point(point1, point2):
#     x = (point1["x"] + point2["x"]) / 2
#     y = (point1["y"] + point2["y"]) / 2
#
#     return {"x": x, "y": y}


point1 = {'x': 0, 'y': 0, 'z': 0}
point2 = {'x': 4, 'y': 4, 'z': 4}
print(get_mid_point(point1, point2))  # {'x': 2, 'y': 2, 'z': 2}
point3 = {'x': -1, 'y': 10, 'z': 5}
point4 = {'x': 0, 'y': -3, 'z': 7}
print(get_mid_point(point3, point4))  # {'x': -0.5, 'y': 3.5, 'z': 6.0}
