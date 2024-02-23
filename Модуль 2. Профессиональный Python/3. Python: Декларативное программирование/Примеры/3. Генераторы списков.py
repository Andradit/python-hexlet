source = range(1, 100)

print(list(source))

print(sum([num ** 2 for num in source if num // 10 >= 1 and num // 10 < 10]))

# print([sum([].append(num ** 2)) for num in source if num // 10 >= 1 and num
# // 10< 10][0]) ---> Error

# print([num += num ** 2 for num in source if num // 10 >= 1 and num // 10 <
# 10]) ---> Error

print(sum([x ** 2 for x in [num for num in source if num // 10 >= 1] if
           x // 10 < 10]))

print(sum(map(lambda num: num ** 2,
              (filter(lambda num: num // 10 >= 1 and num // 10 < 10, source)))))

"""[ <что хотим получить элементом в результативной коллекции>
    for <подколлекция> in <коллекция>
        for <подподколлекция> in <подколлекция>
            for <элемент> in <подподколлекция>
        ....
    ]"""