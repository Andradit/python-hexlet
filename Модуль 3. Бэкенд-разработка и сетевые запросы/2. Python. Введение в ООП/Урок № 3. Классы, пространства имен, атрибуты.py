"""Вам нужно реализовать класс Color, который должен содержать атрибуты red,
green и blue. Значениями этих атрибутов должны быть представления цвета в
цветовой модели RGB. Для получения значений для атрибутов используйте
предоставленную функцию rgb."""


# from solution import Color, rgb
# Color.red  # (255, 0, 0)
# Color.green == rgb(0, 255, 0)  # True
def rgb(red, green, blue):
    return red, green, blue


class Color:
    red = rgb(255, 0, 0)
    green = rgb(0, 255, 0)
    blue = rgb(0, 0, 255)


print(Color.red)
print(Color.green == rgb(0, 255, 0))

'SOLUTION'

# class Color:
#     red = rgb(255, 0, 0)
#     green = rgb(0, 255, 0)
#     blue = rgb(0, 0, 255)
