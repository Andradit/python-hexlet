Напишите запрос, который извлекает из таблицы заказов orders все названия товаров (поле product) и цену (поле price) по
уникальным названиям товаров. Выборка должна быть отсортирована по названию товара в порядке убывания и по цене в
порядке убывания.

Подсказки

Структуру таблицы orders можно посмотреть в файле init.sql

SELECT DISTINCT ON (product)
    product,
    price
FROM orders
ORDER BY product DESC, price DESC;

SOLUTION

-- IDENTICAL!!!