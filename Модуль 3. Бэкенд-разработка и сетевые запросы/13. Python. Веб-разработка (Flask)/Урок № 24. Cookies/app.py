"""Чтобы отличить заказы одного пользователя от другого нужно привязать их к
какому-то уникальному идентификатору. Для этого мы можем использовать механизм
кук и хранить все данные заказа в браузере пользователя или как говорят, на
клиенте.

В этой практике вам нужно будет реализовать корзину сайта с двумя обработчиками
ее содержимого.

src/app.py
Реализуйте два обработчика:

    - POST /cart-items — для добавления товаров в корзину
    - POST /cart-items/clean — для очистки корзины

Корзина должна быть представлена сериализованным в JSON словарем и храниться на
клиенте в куках. В корзине нужно хранить наименование товара и его количество.
Когда товар добавляется, это приводит к увеличению счетчика и редиректу на
главную страницу. Если очистить корзину, это приведет к удалению всех товаров из
корзины и также редиректу на главную страницу.

Структуру данных корзины можно посмотреть в шаблоне src/templates/index.html.

Подсказки
    - для сериализации/десериализации данных используйте json.dumps() и
    json.loads()
    - flask.redirect() возвращает объект ответа Response
    - Работа с Cookies
    - set_cookie()"""
from decorator import append
from flask import Flask, json, redirect, render_template, request, make_response

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    cart = json.loads(request.cookies.get('cart', json.dumps({})))
    return render_template('index.html', cart=cart)


# BEGIN (write your solution here)
@app.post("/cart-items")
def cart_items():
    item_name = request.form['item_name']
    item_id = request.form['item_id']
    cart = json.loads(request.cookies.get("cart", json.dumps({})))
    if item_id in cart:
        cart[item_id]['count'] += 1
    else:
        cart[item_id] = {'name': item_name, 'count': 1}
    encoded_сart = json.dumps(cart)
    response = redirect("/")
    response.set_cookie("cart", encoded_сart)
    return response


@app.post('/cart-items/clean')
def cart_items_clean():
    response = redirect('/')
    response.set_cookie('cart', json.dumps({}))
    return response

# END


'Запуск локального веб-сервера'
if __name__ == '__main__':
    app.run(debug=True)

'SOlUTION'

# BEGIN
# @app.route('/cart-items', methods=['POST'])
# def add_item_to_cart():
#     cart = json.loads(request.cookies.get('cart', json.dumps({})))
#
#     id = request.form['item_id']
#     name = request.form['item_name']
#
#     item = cart.setdefault(id, {'name': name, 'count': 0})
#     item['count'] += 1
#
#     encoded_cart = json.dumps(cart)
#
#     response = redirect('/')
#     response.set_cookie('cart', encoded_cart)
#
#     return response
#
#
# @app.route('/cart-items/clean', methods=['POST'])
# def clean_cart():
#     response = redirect('/')
#     response.delete_cookie('cart')
#
#     return response
# END