'''В этом упражнении вам нужно будет, используя функцию rgb(), реализовать
функцию get_colors(), которая должна вернуть словарь цветов (о цветовой модели
RGB вы можете почитать тут). В словаре должны присутствовать ключи 'red',
'green', 'blue'. Каждому ключу должен соответствовать результат вызова функции
rgb() со значением 255 для соответствующего ключу аргумента. Для построения
каждого цвета используйте только один аргумент!'''

# colors = get_colors()
# colors.keys()
# dict_keys(['red', 'green', 'blue'])
# colors['red']
# 'rgb(255, 0, 0)'
# colors['blue']
# 'rgb(0, 0, 255)'


def rgb(red=0, green=0, blue=0):
    return f'rgb({red}, {green}, {blue})'


print(rgb(green=255))


def get_colors():
    d = {
        'red': rgb(red=255),
        'green': rgb(green=255),
        'blue': rgb(blue=255)
    }
    return d

# SOLUTION
# def get_colors():
#     return {
#         'red': rgb(red=255),
#         'green': rgb(green=255),
#         'blue': rgb(blue=255),
#     }
