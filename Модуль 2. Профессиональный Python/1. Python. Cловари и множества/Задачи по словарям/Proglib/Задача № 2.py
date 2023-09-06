'''Турист собирается в поход. Он сможет нести N кг вещей. Но вещей, которые он
запланировал уложить в рюкзак, оказалось намного больше. Нужно определить,
какие вещи от наиболее тяжелых к самым легким поместятся в рюкзак.'''

things = {'зажигалка': 20,
          'компас': 100,
          'фрукты': 500,
          'рубашка': 300,
          'термос': 1000,
          'аптечка': 200,
          'куртка': 600,
          'бинокль': 400,
          'удочка': 1200,
          'салфетки': 40,
          'бутерброды': 820,
          'палатка': 5500,
          'спальный мешок': 2250,
          'жвачка': 10}


def things_in_bag(weight):
    sorted_weights = sorted(things.items(), key=lambda item: item[1])
    sorted_dict = {k: v for k, v in sorted_weights}
    weight = weight * 1000
    res = []
    for k, v in sorted_dict.items():
        if v <= weight:
            res.append(k)
            weight -= v
    return res


print(things_in_bag(1))
