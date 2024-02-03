"""Реализуйте функцию downcase_file_names(). Она должна принимать на вход
директорию (объект-дерево) и приводить имена всех файлов к нижнему регистру,
причем в корневой директории и во всех вложенных. Функция должна возвращать
результат в виде обработанной директории:"""
import copy

from hexlet.fs import mkdir, mkfile, get_children, get_name, get_meta, is_file
# from solution import downcase_file_names
tree = mkdir('/', [
    mkdir('eTc', [
        mkdir('NgiNx', [], {'size': 4000}),
        mkdir(
            'CONSUL',
            [mkfile('config.JSON', {'uid': 0})],
        ),
    ]),
    mkfile('HOSTS'),
])
# new_tree = downcase_file_names(tree)
# new_file = get_children(new_tree)[1]
# get_name(new_file)  # hosts

"""Подсказки
Придерживайтесь идеи иммутабельности - функция должна быть возвращать 
новое дерево, значит его метаданные должны быть скопированы (deep copy), 
а не ссылаться на оригинальные"""


def downcase_file_names(node):
    if is_file(node):
        return mkfile(get_name(node).lower(), copy.deepcopy(get_meta(node)))
    return mkdir(
        get_name(node),
        list(map(lambda child: downcase_file_names(child), get_children(node))),
        copy.deepcopy(get_meta(node))
    )

'UNDERSTANDABLE SOLUTION'
# def downcase_file_names(node):
#     name = get_name(node)
#     # print(name)
#     new_meta = copy.deepcopy(get_meta(node))
#     # print(new_meta)
#     if is_file(node):
#         new_name = name.lower()
#         return mkfile(new_name, new_meta)
#     children = get_children(node)
#     upd_name = list(map(lambda child: downcase_file_names(child), children))
#     new_tree = mkdir(name, upd_name, new_meta)
#     return new_tree

'SOLUTION'

# def downcase_file_names(node):
#     new_meta = copy.deepcopy(get_meta(node))
#     name = get_name(node)
#     if is_file(node):
#         return mkfile(name.lower(), new_meta)
#     children = get_children(node)
#     new_children = map(downcase_file_names, children)
#     return mkdir(name, list(new_children), new_meta)

print(downcase_file_names(tree))
new_tree = downcase_file_names(tree)
new_file = get_children(new_tree)[1]
print(get_name(new_file))  # hosts