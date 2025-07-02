"""В этом задании вам предстоит добавить флеш-сообщения, которые позволяют
сообщить пользователю о результате его действий.

src/app.py
Реализуйте два обработчика:

    - / — выводит флеш-сообщения в шаблон templates/index.html.
    - /courses — добавляет сообщение Course Added во flash и делает редирект на
    /.

templates/index.html

Реализуйте вывод flash-сообщений"""

from flask import (
    Flask,
    flash,
    get_flashed_messages,
    render_template,
    redirect,
    url_for
)
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')


# BEGIN (write your solution here)
@app.route('/')
def index():
    return render_template('index.html')


@app.post('/courses')
def get_flash():
    flash('Course Added', 'success')
    return redirect(url_for('index'))

# END

'Запуск локального веб-сервера'
if __name__ == '__main__':
    app.run(debug=True)

'SOLUTION'

# @app.route('/')
# def index():
#     messages = get_flashed_messages(with_categories=True)
#     return render_template('index.html', messages=messages)
#
#
# @app.post('/courses')
# def post_courses():
#     flash('Course Added', 'success')
#     return redirect(url_for('index'))
