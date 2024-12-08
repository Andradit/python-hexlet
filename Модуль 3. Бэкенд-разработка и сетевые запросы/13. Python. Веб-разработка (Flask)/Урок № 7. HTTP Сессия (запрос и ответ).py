"""Пейджинг — механизм, который позволяет итерироваться по большим коллекциям
небольшими порциями. Часто встречается в Интернете, например, в результатах
запросов поисковых систем. Пейджинг с точки зрения пользователя выглядит как
параметры запроса: page определяет текущую страницу, а per — количество
элементов на страницу. Имена могут быть и другими, но обычно их называют,
как показано выше. Запрос c page, равным 1, аналогичен запросу без указания
page.

Реализуйте маршрут /companies, по которому отдается список компаний в виде json.
Компании отдаются не все сразу, а только соответствующие текущей запрошенной
странице. По умолчанию выдается 5 результатов на запрос.

Выдаст первые пять компаний
GET /companies

Выдаст компании с 7 по 9
GET /companies?page=3&per=3

Подсказки
    - список компаний лежит в массиве companies;
    - при получении параметров запроса используйте type. Это позволит привести
      полученное значение к определенному типу"""

from flask import Flask, jsonify, request

from data import generate_companies

companies = generate_companies(100)

app = Flask(__name__)


@app.route('/')
def index():
    return "<a href='/companies'>Companies</a>"


# BEGIN (write your solution here)
@app.route('/companies')
def get_companies():
    page = request.args.get('page', 1, type=int)
    per = request.args.get('per', 5, type=int)
    offset = (page - 1) * per
    slice_of_companies = companies[offset:page*per]
    return jsonify(slice_of_companies)

# END

'SOLUTION'

# BEGIN
# @app.route('/companies')
# def get_companies():
#     page = request.args.get('page', 1, type=int)
#     limit = request.args.get('per', 5, type=int)
#     offset = (page - 1) * limit
#     slice_of_companies = companies[offset:page*limit]
#     return jsonify(slice_of_companies)
# # END