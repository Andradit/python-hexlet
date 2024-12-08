"""Напишите тесты для корзины интернет-магазина. В ней используются такие
функции:

    1. make_cart() — создает новую корзину (объект).
    2. add_item(good, count) – добавляет в корзину товары и их количество.
    Товар – это словарь с двумя ключами: название name и стоимость price.
    3. get_items() – возвращает список товаров в формате [{good, count},
    {good, count}, ...].
    4. get_cost() – возвращает стоимость корзины. Общая стоимость корзины
    высчитывается как сумма стоимости всех добавленных товаров с учетом их
    количества.
    5. get_count() – возвращает общее количество товаров в корзине

Корзина реализована таким образом:"""


# cart = make_cart()
# cart.add_item({'name': 'car', 'price': 3}, 5)
# cart.add_item({'name': 'house', 'price': 10}, 2)
# len(cart.get_items())  # 2
# cart.get_cost()  # 35
# # Считаем, что все товары уникальные
# # Товар с таким же названием добавляется в корзину новой позицией
# cart.add_item({'name': 'house', 'price': 10}, 1)
# len(cart.get_items())  # 3
# cart.get_cost()  # 45

# def cart():
#     return []

from cart import get_implementations

make_cart = get_implementations()

def test_cart():
    cart = make_cart()
    cart.add_item({'name': 'car', 'price': 3}, 5)
    cart.add_item({'name': 'house', 'price': 10}, 2)
    assert len(cart.get_items()) == 2
    assert cart.get_cost() == 35
    cart.add_item({'name': 'house', 'price': 10}, 1)
    assert len(cart.get_items()) == 3
    assert cart.get_cost() == 45


'SOLUTION'

# def test_cart():
#     cart = make_cart()
#     assert not len(cart.get_items())
#
#     cart.add_item({'name': 'car', 'price': 3}, 5)
#     assert len(cart.get_items()) == 1
#     assert cart.get_cost() == 15
#     assert cart.get_count() == 5
#
#     cart.add_item({'name': 'house', 'price': 10}, 2)
#     assert len(cart.get_items()) == 2
#     assert cart.get_cost() == 35
#     assert cart.get_count() == 7
