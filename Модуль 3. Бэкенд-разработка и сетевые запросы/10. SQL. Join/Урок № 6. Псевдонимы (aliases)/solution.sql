В базе данных есть две таблицы – товары и категории товаров. Таблицы имеют следующую структуру:

Таблица categories

id	name
1	food
2	...

Таблица products

id	category_id	name
1	1	lemon
2	2	...

Поле products.category_id ссылается на поле categories.id

Составьте запрос, который получит все товары с категорией, в которой он находится. Итоговая таблица должна иметь поля
product и category. Отсортируйте выборку по названию категории и названию товара

Подсказки

Структуру таблиц можно посмотреть в файле init.sql

SELECT
    prod.name AS product,
    cat.name AS category
FROM products AS prod
INNER JOIN categories AS cat
    ON prod.category_id = cat.id
ORDER BY category, product;


SOLUTION

-- SELECT
--     products.name AS product,
--     categories.name AS category
-- FROM products
-- INNER JOIN categories
--     ON categories.id = products.category_id
-- ORDER BY category, product;
