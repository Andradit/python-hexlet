"""В этой практике вам предстоит попрактиковаться в CREATE операций CRUD. Чтобы
добавить данные используется форма создания ресурса. Также введенные данные
обязательно нужно провалидировать, чтобы в хранилище не попала некорректная
информация.

src/app.py
Реализуйте следующие обработчики:

    - форма создания нового поста: GET /posts/new
    - создание поста: POST /posts

Посты содержат два поля: title и body. Они обязательны к заполнению. Валидация
уже написана, но не забудьте про вывод ошибок валидации.

После каждого успешного действия нужно добавлять флеш-сообщение 'Post has been
created' и выводить его на списке постов.

templates/posts/new.html

Форма для создания поста

Подсказки

    - чтобы работать с репозиторием в обработчике, его нужно инициализировать по
    примеру в posts_get()
    - чтобы сохранить пост, используйте метод репозитория save()
    - для обработки незаполненных полей можно воспользоваться встроенным в
    шаблонизатор фильтром default()"""

import os

from flask import (
    Flask,
    flash,
    get_flashed_messages,
    redirect,
    render_template,
    request,
    url_for,
)
from repository import PostsRepository
from validator import validate

app = Flask(__name__)
app.config['SECRET_KEY'] = 'aasdasddvafdsf'


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


# BEGIN (write your solution here)
@app.route('/posts/new')
def new_post():
    post = []
    errors = []
    return render_template('posts/new.html', post=post, errors=errors)


@app.post('/posts')
def create_post():
    repo = PostsRepository()
    data = request.form.to_dict()
    errors = validate(data)
    if errors:
        return render_template(
            'posts/new.html',
            post=data,
            errors=errors,
        ), 422
    repo.save(data)
    flash('Post has been created', 'success')
    return redirect(url_for('create_post'))


# END

'Запуск локального веб-сервера'
if __name__ == '__main__':
    app.run(debug=True)
