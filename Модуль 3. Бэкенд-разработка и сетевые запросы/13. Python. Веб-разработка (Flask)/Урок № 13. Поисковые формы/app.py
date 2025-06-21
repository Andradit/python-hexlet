"""Ни один сайт не обходится без поисковой строки. Зачастую, поиск работает по
принципу приближенного соответствия строк.

В этом упражнении вам нужно будет создать форму для поиска имени пользователя,
которое начинается с введенных букв.

app.py

Реализуйте обработчик по маршруту /users, который формирует список
пользователей. Обработчик поддерживает фильтрацию через параметр term, в котором
передается first_name. Он возвращает все совпадения по началу имени
пользователя. Список пользователей доступен в переменной users.

templates/users/index.html

Реализуйте вывод списка пользователей и формы для фильтрации.

Если форма пустая, то должен выводиться список всех пользователей. Если
заполнена, то отфильтрованный по совпадениям.

Поле ввода должно сохранять введенное значение.

Примечания
    - поиск должен быть регистронезависимым"""

from flask import Flask, render_template, request

from data import generate_users

users = generate_users(100)

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


# BEGIN (write your solution here)
@app.route('/users')
def get_user():
    query = request.args.get('term')
    filtered_user = []
    if query:
        for user in users:
            if user['first_name'].lower().startswith(query.lower()):
                filtered_user.append(user)
        return render_template('users/index.html',
                               users=filtered_user, search=query)
    return render_template('users/index.html', users=users)


# END

'Запуск локального веб-сервера'
# if __name__ == '__main__':
#     app.run(debug=True)

'ALTERNATIVE SOLUTION'
# @app.route('/users')
# def get_user():
#     term = request.args.get('term')
#     if term:
#         filtered_user = [user for user in users if
#                          user['first_name'].lower().startswith(term.lower())]
#         print(filtered_user)
#         return render_template('users/index.html',
#                                users=filtered_user, search=term)
#     return render_template('users/index.html', users=users)

'SOLUTION'
# @app.route('/users')
# def get_users():
#     result = users
#     search = request.args.get('term', '')
#     if search:
#         result = [user for user in users if filter_name(user, search)]
#
#     return render_template(
#         'users/index.html',
#         users=result,
#         search=search,
#     )
