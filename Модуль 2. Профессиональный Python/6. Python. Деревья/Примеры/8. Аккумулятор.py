from hexlet import fs

tree = fs.mkdir('/', [
    fs.mkdir('etc', [
        fs.mkdir('apache'),
        fs.mkdir('nginx', [
            fs.mkfile('nginx.conf'),
        ]),
        fs.mkdir('consul', [
            fs.mkfile('config.json'),
            fs.mkdir('data'),
        ]),
    ]),
    fs.mkdir('logs'),
    fs.mkfile('hosts'),
])


def find_empty_dir_paths(tree):
    name = fs.get_name(tree)
    # Получаем детей узла (директории)
    children = fs.get_children(tree)
    # Если детей нет, то возвращаем директорию
    if len(children) == 0:
        return name
    # Фильтруем файлы, они нас не интересуют
    dir_names = list(filter(fs.is_directory, children))
    # Ищем пустые директории внутри текущей
    empty_dir_names = map(find_empty_dir_paths, dir_names)
    # flatten выправляет список, так что он становится плоским
    return fs.flatten(empty_dir_names)


print(find_empty_dir_paths(tree))

tree = fs.mkdir('/', [
    fs.mkdir('etc', [
        fs.mkdir('apache'),
        fs.mkdir('nginx', [
            fs.mkfile('nginx.conf'),
        ]),
        fs.mkdir('consul', [
            fs.mkfile('config.json'),
            fs.mkdir('data'),
        ]),
    ]),
    fs.mkdir('logs'),
    fs.mkfile('hosts'),
])


def find_empty_dir_paths(tree):
    # Внутренняя функция, которая может передавать аккумулятор
    # Аккумулятором выступает depth, переменная, содержащая текущую глубину
    def walk(node, depth):
        name = fs.get_name(node)
        children = fs.get_children(node)
        # Если детей нет, то возвращаем директорию
        if len(children) == 0:
            return name
        # Если это второй уровень вложенности, и директория не пустая
        # то не имеет смысла смотреть дальше
        if depth == 2:
            # Почему возвращается именно пустой список?
            # Потому что снаружи выполняется flatten
            # Он раскрывает пустые списки
            return []
        # Оставляем только директории
        dir_paths = filter(fs.is_directory, children)
        # Не забываем увеличивать глубину
        output = list(map(
            lambda child: walk(child, depth + 1),
            dir_paths,
        ))
        # Перед возвратом "выпрямляем" список
        return fs.flatten(output)

    # Начинаем с глубины 0
    return walk(tree, 0)


print(find_empty_dir_paths(tree))
