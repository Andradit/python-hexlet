from flask import Flask, render_template
from flask import request

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


users = [
    {'id': 1, 'name': 'mike'},
    {'id': 2, 'name': 'mishel'},
    {'id': 3, 'name': 'adel'},
    {'id': 4, 'name': 'keks'},
    {'id': 5, 'name': 'kamila'}
]


@app.route('/users')
def get_users():
    term = request.args.get('term')
    filtered_users = [user for user in users if term in user]
    return render_template(
        'users/index.html',
        users=filtered_users,
        search=term
    )
