"""Реализуйте функцию compress_images(). Она должна принимать на вход
директорию, находить внутри нее картинки и уменьшать свойство size в их
метаданных в два раза. Функция должна вернуть обновленную директорию со
сжатыми картинками и всеми остальными данными, которые были внутри этой
директории.

Картинками считаются все файлы, заканчивающиеся на .jpg:"""
import copy

from hexlet.fs import get_children, get_meta, get_name, is_file, mkdir, mkfile

#
# tree = mkdir(
#     'my documents',
#     [
#         mkfile('avatar.jpg', {'size': 100}),
#         mkfile('photo.jpg', {'size': 150}),
#     ],
#     {'hide': False}
# )

tree = mkdir('my documents', [
    mkfile(
        'avatar.jpg',
        {'size': 100, 'attributes': {'hide': False, 'read_only': True}},
    ),
    mkdir('presentations'),
], {'owner': 'hexlet'})


# compress_images(tree)
# {
#     'name': 'my documents',
#     'type': 'directory',
#     'children': [
#         {'name': 'avatar.jpg', 'meta': {'size': 50}, 'type': 'file'},
#         {'name': 'photo.jpg', 'meta': {'size': 75}, 'type': 'file'},
#     ],
#     'meta': {'hide': False},
# }
# print(tree)

# def compress_images(file):
#     new_children = copy.deepcopy(get_children(file))
#     new_meta = copy.deepcopy(get_meta(file))
#
#     for descendant in new_children:
#         if descendant['name'].endswith('.jpg'):
#             meta_of_des = descendant['meta']
#             if 'size' in meta_of_des:
#                 meta_of_des['size'] //= 2
#
#     new_file = mkdir(get_name(file), new_children, new_meta)
#
#     return new_file

def compress_images(file):
    new_children = copy.deepcopy(get_children(file))

    for descendant in new_children:
        if descendant['name'].endswith('.jpg'):
            if 'size' in descendant['meta']:
                descendant['meta']['size'] //= 2

    new_file = mkdir(get_name(file), new_children, copy.deepcopy(get_meta(file)))

    return new_file

# old_file = get_children(tree)[0]
# print(old_file)
# print(get_meta(old_file)['attributes']['hide'])
print(compress_images(tree))

'SOLUTION'
# def compress_images(tree):
#     children = get_children(tree)
#
#     def reduce_image_size(node):
#         name = get_name(node)
#         if not is_file(node) or not name.endswith('.jpg'):
#             return node
#         meta = get_meta(node)
#         new_meta = copy.deepcopy(meta)
#         new_meta['size'] //= 2
#         return mkfile(name, new_meta)
#
#     new_children = map(reduce_image_size, children)
#     new_meta = copy.deepcopy(get_meta(tree))
#     return mkdir(get_name(tree), list(new_children), new_meta)
#
#
# print(compress_images(tree))
