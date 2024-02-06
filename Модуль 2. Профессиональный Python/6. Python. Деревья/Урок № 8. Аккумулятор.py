"""Реализуйте функцию find_files_by_name(). Она должна принимать на вход
файловое дерево и подстроку, а затем возвращать список файлов, имена которых
содержат эту подстроку. Функция должна вернуть полные пути файлам:"""
import math
import os.path
from hexlet.fs import mkdir, mkfile, flatten, get_children, get_name, is_file

tree = mkdir('/', [
    mkdir('etc', [
        mkdir('apache'),
        mkdir('nginx', [
            mkfile('nginx.conf', {'size': 800}),
        ]),
        mkdir('consul', [
            mkfile('config.json'),
            mkfile('data'),
            mkfile('raft'),
        ]),
    ]),
    mkfile('hosts', {'size': 3500}),
    mkfile('resolve', {'size': 1000}),
])
# find_files_by_name(tree, 'co')
# ['/etc/nginx/nginx.conf', '/etc/consul/config.json']

"""Подсказки
- для реализации этой логики вам понадобится аккумулятор, в котором будет
храниться путь от корня до текущего узла. При проваливании внутрь директорий к
нему добавляется имя текущей директории. В остальном логика работы идентична
примеру из теории;
- переменную с путем от корня до текущего узла можно назвать ancestry;
- для построения путей используйте функцию os.path.join()"""
from functools import reduce


# def strings(node, sub_string):
#     if is_file(node) and sub_string in get_name(node):
#         return get_name
#     return list(map(strings(sub_string), get_children(node)))
#
# print(strings(tree, 'co'))

# def get_sub(node, sub_str):
#     if is_file(node) and sub_str in get_name(node):
#         return get_name(node)

def find_files_by_name(tree, sub_string):
    def walk(node, depth):
        name = get_name(node)
        children = get_children(node)

        if name.find(sub_string) > -1 and is_file(node):
            depth = os.path.join(depth, name)
            return depth

        depth = os.path.join(depth, name)
        ancestry = list(map(lambda child: walk(child, depth), children))
        
        return flatten(ancestry)

    return walk(tree, '')


'SOLUTION'


def find_files_by_name(tree, substr):
    def walk(node, ancestry):
        name = get_name(node)
        new_ancestry = os.path.join(ancestry, name)

        if is_file(node):
            return [] if name.find(substr) < 0 else new_ancestry

        children = get_children(node)
        paths = map(lambda child: walk(child, new_ancestry), children)

        return flatten(paths)

    return walk(tree, '')


print(find_files_by_name(tree, 'co'))
# ['/etc/nginx/nginx.conf', '/etc/consul/config.json']
