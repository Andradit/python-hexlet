"""В этой практике вам предстоит попрактиковаться в UPDATE операций CRUD. Для
обновления ресурса сперва его нужно получить из хранилища и заполнить форму
редактирования, а затем обновить, получив и провалидировав новые данные из
формы.

Также оповестите пользователя об успешной операции с помощью флеш-сообщений.

src/app.py
Реализуйте следующие обработчики:

    - форма редактирования поста: GET /posts/<id>/update
    - обновление поста: POST /posts/<id>/update

Посты содержат два поля: title и body. Они обязательны к заполнению. Валидация
уже написана, но не забудьте про вывод ошибок валидации.

После каждого успешного действия нужно добавлять флеш-сообщение 'Post has been
updated' и выводить его на списке постов.

templates/posts/index.html
Реализуйте вывод списка постов. В списке выводится title поста и ссылка Edit на
страницу его редактирования.

templates/posts/edit.html
Форма для редактирования поста. Общая часть формы уже выделена в шаблон
form.html, подключите его по аналогии с templates/posts/new.html.

Подсказки
    - include
    - для редиректов в обработчиках используйте именованный роутинг"""

from flask import (
    Flask,
    flash,
    get_flashed_messages,
    make_response,
    redirect,
    render_template,
    request,
    url_for,
)
import os

from repository import PostsRepository
from validator import validate

app = Flask(__name__)
app.config['SECRET_KEY'] = 'asadfsdfdsfsd'


@app.route('/')
def index():
    return render_template('index.html')


@app.get('/posts')
def posts_get():
    repo = PostsRepository()
    messages = get_flashed_messages(with_categories=True)
    posts = repo.content()
    return render_template(
        'posts/index.html',
        posts=posts,
        messages=messages,
    )


@app.route('/posts/new')
def new_post():
    post = {}
    errors = {}
    return render_template(
        'posts/new.html',
        post=post,
        errors=errors,
    )


@app.post('/posts')
def posts_post():
    repo = PostsRepository()
    data = request.form.to_dict()
    errors = validate(data)
    if errors:
        return render_template(
            'posts/new.html',
            post=data,
            errors=errors,
        ), 422
    id = repo.save(data)
    flash('Post has been created', 'success')
    resp = make_response(redirect(url_for('posts_get')))
    resp.headers['X-ID'] = id
    return resp


# BEGIN (write your solution here)
@app.get('/posts/<id>/update')
def post_edit(id):
    repo = PostsRepository()
    post = repo.find(id)
    messages = get_flashed_messages(with_categories=True)
    errors = validate(post)
    return render_template(
        'posts/edit.html',
        post=post,
        messages=messages,
        errors=errors,
    )


@app.post('/posts/<id>/update')
def post_update(id):
    repo = PostsRepository()
    post = repo.find(id)
    data = request.form.to_dict()
    errors = validate(data)
    if errors:
        return render_template(
            "posts/edit.html",
            post=post,
            errors=errors,
        ), 422
    post["title"] = data["title"]
    post["body"] = data["body"]
    repo.save(post)
    flash("Post has been updated", "success")
    return redirect(url_for("posts_get"))


# END


'Запуск локального веб-сервера'
if __name__ == '__main__':
    app.run(debug=True)


'SOLUTION'

# BEGIN
# @app.route('/posts/<id>/update', methods=['GET', 'POST'])
# def post_update(id):
#     repo = PostsRepository()
#     post = repo.find(id)
#
#     if request.method == 'GET':
#         return render_template(
#             'posts/edit.html',
#             post=post,
#             errors={},
#         )
#
#     if request.method == 'POST':
#         data = request.form.to_dict()
#         data['id'] = id
#
#         errors = validate(data)
#         if errors:
#             return render_template(
#                 'posts/edit.html',
#                 post=data,
#                 errors=errors,
#             ), 422
#
#         post['title'] = data.get('title', '')
#         post['body'] = data.get('body', '')
#         repo.save(post)
#         flash('Post has been updated', 'success')
#         return redirect(url_for('posts_get'))
# END
