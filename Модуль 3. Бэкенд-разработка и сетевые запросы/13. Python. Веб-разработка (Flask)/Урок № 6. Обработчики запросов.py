"""С ростом веб-приложения нужно выводить разные данные на отдельных
страницах, чтобы удобно их представлять.

В этом упражнении вам нужно вывести список двух ресурсов: телефонов и доменов.

Добавьте обработчики:

    - /phones — возвращает список телефонов, которые содержатся в переменной
    phones, закодированной в json
    - /domains — возвращает список доменов, которые содержатся в переменной
    domains, закодированной в json

Подсказки
Сериализация данных в json и формирование объекта Response:
flask.json.jsonify()"""

from faker import Faker
from flask import Flask, jsonify

fake = Faker()
fake.seed_instance(1234)

domains = [fake.domain_name() for i in range(10)]
phones = [fake.phone_number() for i in range(10)]

app = Flask(__name__)


@app.route('/')
def index():
    return 'go to the /phones or /domains'


# BEGIN (write your solution here)
@app.route("/phones")
def get_phone_numbers():
    return jsonify(phones)


@app.route("/domains")
def get_domain_names():
    return jsonify(domains)


# END

'SOLUTION'

# BEGIN
# @app.route('/phones')
# def get_phones():
#     return jsonify(phones)

# @app.route('/domains')
# def get_domains():
#     return jsonify(domains)
# END
