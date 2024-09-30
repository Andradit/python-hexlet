"""Ваша задача - создать класс RGB, который представляет цвет в формате RGB.
У класса должны быть три атрибута: red, green, и blue. Каждый из них по
умолчанию равен 0. Затем создайте три переменные: red, green, и blue, каждая
должна быть экземпляром класса RGB. В переменной red атрибут red должен быть
установлен в 255, а green и blue - в 0. Аналогично делаются атрибуты для
green и blue.

Цель - чтобы ваш код работал с этим примером:"""


# import solution
# def rgb2tuple(rgb):
#     if isinstance(rgb, solution.RGB):
#          return rgb.red, rgb.green, rgb.blue
#
# rgb2tuple(42)
# rgb2tuple(solution.red)  # (255, 0, 0)
# rgb2tuple(solution.green)  # (0, 255, 0)
# rgb2tuple(solution.blue)  # (0, 0, 255)


class RGB:
    red = 0
    green = 0
    blue = 0


red, green, blue = RGB(), RGB(), RGB()
red.__dict__['red'] = 255
green.__dict__['green'] = 255
blue.__dict__['blue'] = 255

'SOLUTION'

# class RGB:
#     # в случае иммутабельных значений можно себе позволить
#     # сделать так
#     red = green = blue = 0
#
#
# red, green, blue = RGB(), RGB(), RGB()
# red.red = 255
# green.green = 255
# blue.blue = 255
