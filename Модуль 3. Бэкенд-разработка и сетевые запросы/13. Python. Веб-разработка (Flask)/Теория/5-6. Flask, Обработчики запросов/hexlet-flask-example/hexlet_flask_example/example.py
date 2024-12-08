from flask import Flask, render_template

# Это callable WSGI-приложение
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Welcome to Flask!'


@app.get('/users')
def users_get():
    return 'GET /users'


@app.post('/users')
def users_post():
    return 'Users', 302


@app.route('/courses/<id>')
def courses_show(id):
    return f'Course id: {id}'


# @app.route('/users/<id>')
# def users_show(id):
#     return render_template('index.html', name=id)

@app.route('/users/<id>')
def users_id(id):
    return render_template('users/show.html', num=id)

