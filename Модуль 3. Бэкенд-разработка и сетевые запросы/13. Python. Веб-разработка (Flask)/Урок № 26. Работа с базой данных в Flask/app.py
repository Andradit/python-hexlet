"""В этой практике вам предстоит попрактиковаться в операциях CRUD, работая с
базой данных. Благодаря абстракции репозитория, порядок работы не будет
отличаться от предыдущих практик.

src/app.py
Добавьте обработчики для добавления нового товара и для просмотра информации о
товаре:

    - GET запрос на адрес /products/new — отрисовка формы добавления нового
    товара
     - GET запрос на адрес /products/<id> — просмотр информации о конкретном
     товаре
    - POST запрос на адрес /products — создание нового товара

Для работы с базой используйте репозиторий

Продукт содержат два поля: title и price. Они обязательны к заполнению.
Валидация уже написана, но не забудьте про вывод ошибок валидации.

templates/products/index.html
Реализуйте вывод списка товаров в виде таблицы. В таблице выводится title и
price товара.

templates/products/new.html
Шаблон для создания товара. Общая часть формы уже выделена в form.html,
подключите ее.

Подсказки
    - Include
    - для редиректов в обработчиках используйте именованный роутинг"""

from flask import (
    Flask,
    flash,
    redirect,
    render_template,
    request,
    url_for,
)
import os

from repository import get_db, ProductsRepository
from validator import validate

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['DATABASE_URL'] = os.getenv('DATABASE_URL')

repo = ProductsRepository(get_db(app))


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/products')
def products():
    products = repo.get_entities()
    return render_template('products/index.html', products=products)


# BEGIN (write your solution here)
@app.route('/products/new', methods=['GET'])
def new_product():
    return render_template('products/new.html', product={}, errors={})


@app.route('/products/<int:id>', methods=['GET'])
def get_product(id):
    product = repo.find(id)
    if product is None:
        return 'Product not found', 404
    return render_template('products/show.html', product=product)


@app.route('/products', methods=['POST'])
def add_product():
    data = request.form.to_dict()
    errors = validate(data)
    if not errors:
        product = {"title": data["title"], "price": data["price"]}
        repo.save(product)
        flash('Product has been created', 'success')
        return redirect(url_for("products"))
    return render_template("products/new.html", product=data,
                           errors=errors), 422
# END

'SOLUTION'

# BEGIN
# @app.route('/products/new')
# def new_product():
#     return render_template('products/new.html', product={}, errors=[])
#
#
# @app.route('/products/<int:id>')
# def show_product(id):
#     product = repo.find(id)
#     if product is None:
#         return 'Product not found', 404
#     return render_template('products/show.html', product=product)
#
#
# @app.route('/products', methods=['POST'])
# def create_product():
#     product_data = request.form.to_dict()
#
#     errors = validate(product_data)
#
#     if not errors:
#         product = product_data
#         repo.save(product)
#         flash('Product has been created', 'success')
#         return redirect(url_for('products'))
#
#     return render_template(
#         'products/new.html',
#         product=product_data,
#         errors=errors
#         ), 422
# END