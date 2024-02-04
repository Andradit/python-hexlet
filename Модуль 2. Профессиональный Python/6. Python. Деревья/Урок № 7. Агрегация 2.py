"""В Linux, MacOS и многих операционных системах существует утилита du. Она
умеет подсчитывать, сколько места занимают указанные файлы и директории.
Например, так:"""

#  tmp$ du -sh *
#  97k    .venv
#   0B    com.docker.vmnetd.socket
#  10M    credo
# 4.0K    debug.mjs
#   0B    filesystemui.socket
# 4.0K    index.py
#  88K    poetry-lock.json
#  22M    taxdome

"""Перед решением этого задания обязательно попрактикуйтесь с этой утилитой в 
терминале, посмотрите ее опции через man du. Экспериментировать нужно в 
локально установленной операционной системе.

Реализуйте функцию du. Она должна принимать на вход директорию и возвращать:

- список всех директорий и файлов, которые вложены в указанную директорию на 
один уровень.
- размер всей директории, который складывается из сумм всех размеров файлов, 
находящихся внутри во всех подпапках.

Так это выглядит в коде:"""

from hexlet.fs import mkdir, mkfile, get_children, get_meta, get_name, is_file

# from solution import du
# tree = mkdir('/', [
#     mkdir('etc', [
#         mkdir('apache'),
#         mkdir('nginx', [
#             mkfile('nginx.conf', {'size': 800}),
#         ]),
#         mkdir('consul', [
#             mkfile('.config.json', {'size': 1200}),
#             mkfile('data', {'size': 8200}),
#             mkfile('raft', {'size': 80}),
#         ]),
#     ]),
#     mkfile('hosts', {'size': 3500}),
#     mkfile('resolve', {'size': 1000}),
# ])
# du(tree)  # [('etc', 10280), ('hosts', 3500), ('resolve', 1000)]
tree = mkdir('/', [
    mkdir('etc', [
        mkdir('apache'),
        mkdir('nginx', [
            mkfile('nginx.conf', {'size': 800}),
        ]),
        mkdir('consul', [
            mkfile('.config.json', {'size': 1200}),
            mkfile('data', {'size': 8200}),
            mkfile('raft', {'size': 80}),
        ]),
    ]),
    mkfile('hosts', {'size': 3500}),
    mkfile('resolve', {'size': 1000}),
])

"""Примечания
- размер файла задается в метаданных, при этом сами папки размера не имеют
- в структуре результирующего cписка каждый элемент является кортежем 
с двумя значениями — именем директории и размером файлов внутри
- результат отсортирован по размеру в обратном порядке — сверху тяжелые, 
снизу легкие

Подсказки
sort"""


def get_files_size(tree):
    if is_file(tree):
        file_meta = get_meta(tree)
        return file_meta['size']
    children = get_children(tree)
    return sum(list(map(get_files_size, children)))


# print(get_files_size(tree))


def du(tree):
    children = get_children(tree)
    result = list(map(
        lambda child: (get_name(child), get_files_size(child)), children)
    )
    return sorted(result, key=lambda x: x[1], reverse=True)


# print(compress_images(tree))
print(du(get_children(tree)[0]))
# [('consul', 9480), ('nginx', 800), ('apache', 0)]

print(du(tree))  # [('etc', 10280), ('hosts', 3500), ('resolve', 1000)]
