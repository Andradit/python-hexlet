"""В этой практике вам предстоит попрактиковаться в части READ операций CRUD.
Обычно "чтение" предполагает вывод всей категории ресурсов (списка
пользователей, постов, комментариев) и детальный вывод конкретного ресурса
(личная страничка пользователя). Для удобства также используется пейджинг с
переходами "вперед" и "назад".

src/app.py

Реализуйте следующие обработчики:

    - список постов: /posts
    - конкретный пост /posts/<slug>, например,
    /posts/python-flask-crude-exercise

Посты находятся в репозитории repo. Каждый пост содержит внутри себя четыре
поля:

    - id
    - title — имя поста
    - body — содержание поста
    - slug — слаг

В списке постов должны отображаться заголовки постов. Список нужно вывести с
пейджингом по пять постов на странице. На первой странице — первые пять постов,
на второй — вторые пять и так далее. Переключение между страницами нужно сделать
с помощью двух ссылок: назад и вперед. То, какая сейчас страница открыта,
определяется параметром page. По умолчанию загружается первая страница.

Каждый пост из списка ведет на страницу конкретного поста. Страница конкретного
поста отображает данные поста и позволяет вернуться на список. Если поста нет,
то обработчик должен вернуть код ответа 404 и текст 'Page not found'.

templates/posts/index.html

Выведите список постов. Для каждого поста также нужно вывести ссылку, которая
ведет на отображение — show. Ссылка представлена в виде слага. Не забудьте также
добавить блок с переключением страниц.

Пример вывода:"""

# <ul>
#     <li>
#       <a href="/flask-101">Flask Intro</a>
#     </li>
#     <li>
#       <a href="/flask-crud-lesson">Flask CRUD</a>
#     </li>
# </ul>

"""templates/posts/show.html

Вывод информации о конкретном посте. Выводить только имя и содержимое поста.

Пример вывода:"""

# <body>
# <a href="/posts">Posts</a>
#   <h1>Flask CRUD</h1>
#   <div>Hello, today we're gonna talk about CRUD in Flask</div>
# </body>

"""Подсказки
    - для реализации пейджинга понадобится извлечь все посты из репозитория с
    помощью метода content()
    - переход между страницами реализуется с помощью параметра запроса ?page=
    - If Expresion
    - для поиска поста по slug используйте метод репозитория find()"""

from flask import Flask, render_template, request
from repository import PostsRepository

app = Flask(__name__)

repo = PostsRepository(50)


@app.route('/')
def index():
    return render_template('index.html')


# BEGIN (write your solution here)
@app.route('/posts')
def posts():
    page = request.args.get('page', 1, type=int)
    per = request.args.get('per', 5, type=int)
    offset = (page - 1) * per
    all_posts = repo.content()[offset:page * per]
    return render_template('posts/index.html', posts=all_posts,
                           page=page)


@app.route('/posts/<slug>')
def get_post(slug):
    post = repo.find(slug)
    if not post:
        return 'Page not found', 404
    return render_template('posts/show.html', post=post)


# END

'Запуск локального веб-сервера'
# if __name__ == '__main__':
#     app.run(debug=True)

'SOLUTION'

# BEGIN
# @app.get('/posts')
# def posts():
#     per = 5
#     page = request.args.get('page', 1, type=int)
#     offset = (page - 1) * per
#     all_posts = repo.content()
#     posts_at_page = all_posts[offset:page * per]
#     return render_template(
#         'posts/index.html',
#         page=page,
#         posts=posts_at_page,
#         )
#
#
# @app.get('/posts/<slug>')
# def get_post(slug):
#     post = repo.find(slug)
#     if not post:
#         return 'Page not found', 404
#     return render_template('posts/show.html', post=post)
# END
