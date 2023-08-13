"""В рамках этого испытания вы реализуете небольшой набор функций, работающих с отрезками прямых на двухмерной плоскости. Отрезок в нашем случае будет кодироваться в виде пары пар и выглядеть как-то так: ((x1, y1), (x2, y2)) (вложенные пары — это концы отрезка). Вам нужно реализовать четыре функции:

is_degenerated() должна возвращать истину, если отрезок вырожден в точку (начало и конец совпадают)
is_vertical() должна возвращать истину, если отрезок — вертикальный
is_horizontal() должна возвращать истину, если отрезок — горизонтальный
is_inclined() должна возвращать истину, если отрезок — наклонный (не вертикальный и не горизонтальный)"""


def is_degenerated(line):
    (x1, y1), (x2, y2) = line
    return (x1, y1) == (x2, y2)


def is_vertical(line):
    (x1, y1), (x2, y2) = line
    return x1 == x2 and y1 != y2


def is_horizontal(line):
    (x1, y1), (x2, y2) = line
    return x1 != x2 and y1 == y2


def is_inclined(line):
    (x1, y1), (x2, y2) = line
    return x1 != x2 and y1 != y2

# def is_vertical(line):  ----------------------------> solution
#     (x1, y1), (x2, y2) = line
#     # ^ sometimes it is just fine to unpack such nested structures
#     return x1 == x2 and y1 != y2

# def is_horizontal(line):
#     (x1, y1), (x2, y2) = line
#     return x1 != x2 and y1 == y2

# def is_degenerated(line):
#     p1, p2 = line
#     return p1 == p2

# def is_inclined(line):
#     return not (
#         is_vertical(line) or is_horizontal(line) or is_degenerated(line)
#     )


line1 = (0, 10), (100, 130)
print(is_vertical(line1))  # False
print(is_horizontal(line1))  # False
print(is_degenerated(line1))  # False
print(is_inclined(line1))  # True

line2 = (42, 1), (42, 2)
print(is_vertical(line2))  # True

line3 = (100, 50), (200, 50)
print(is_horizontal(line3))  # True


line = (15, 5), (15, -5)  # VERTICAL
print(is_vertical(line))

line = (5, 15), (-5, 15)  # HORIZONTAL
print(is_horizontal(line))

line = (42, 100), (42, 100)  # DEGENERATED
print(is_degenerated(line))

line = (0, 0), (1, 1)  # INCLINED
print(is_inclined(line))
