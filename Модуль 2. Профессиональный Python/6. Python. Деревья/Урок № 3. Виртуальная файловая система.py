"""Реализуйте функцию generate, которая создает такую файловую структуру:"""

# Обратите внимание на метаданные ниже

# python - package  # Директория (метаданные: {'hidden': True})
# ├── Makefile  # Файл
# ├── README.md  # Файл
# ├── dist  # Пустая директория
# ├── tests  # Директория
# │   └── test_solution.py  # Файл
# ├── pyproject.toml  # Файл
# └──.venv  # Директория (метаданные: {'owner': 'root', 'hidden': False})
#     └── lib  # Директория
#         └── python3.6 # Директория
#             └── site - packages  # Директория
#                 └── hexlet - python - package.egg - link  # Файл

from hexlet.fs import mkdir, mkfile


def generate():
    tree = mkdir('python-package', [
        mkfile('Makefile'),
        mkfile('README.md'),
        mkdir('dist', []),
        mkdir('tests', [
            mkfile('test_solution.py'),
        ]),
        mkfile('pyproject.toml'),
        mkdir('.venv', [
            mkdir('lib', [
                mkdir('python3.6', [
                    mkdir('site-packages', [
                        mkfile('hexlet-python-package.egg-link')
                    ])
                ])
            ])
        ], {'owner': 'root', 'hidden': False}),
    ], {'hidden': True})
    return tree
