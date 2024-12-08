"""Чтобы выводить детальную информацию по каждому отдельному ресурсу какой-то
категории (студенты, курсы, уроки), используются динамические обработчики.

В этом упражнении вам нужно будет создать обработчик для вывода информации по
каждой компании из списка.

src/app.py
Реализуйте маршрут /companies/<id>, по которому отдается json представление
компании. Компания извлекается из списка companies. Каждая компания представлена
словарём, у которого есть числовой (то есть тип данных – число) ключ id:"""

"Пример"
# Гипотетический пример показывающий структуру
# companies = [
#   {
#     'id': 4,
#     # другие элементы словаря
#   },
#   {
#     'id': 2,
#     # другие элементы словаря
#   },
#   {
#     'id': 8,
#     # другие элементы словаря
#   },
# ]

"""Если компания с таким идентификатором не существует, то сайт должен вернуть
ошибку 404 (страница с HTTP кодом 404) и текстом Page not found.

Подсказки
Для указания статуса ответа обработчик должен возвращать кортеж, первое значение
которого тело ответа, а второе значение - статус ответа. Подробнее об
ответах."""

from flask import Flask, jsonify

from data import generate_companies

companies = generate_companies(100)

app = Flask(__name__)


@app.route('/')
def index():
    return 'open something like (you can change id): /companies/5'


# BEGIN (write your solution here)
@app.route('/companies/<int:company_id>')
def get_comp_id(company_id):
    for c in companies:
        if c['id'] == company_id:
            return jsonify(c)
    return 'Page not found', 404
# END

'SOLUTION'

# BEGIN
# @app.route('/companies/<int:id>')
# def get_company(id):
#     filtered_companies = filter(lambda company: company['id'] == id, companies)
#     company = next(filtered_companies, None)
#
#     if company is None:
#         return 'Page not found', 404
#
#     return jsonify(company)
# END