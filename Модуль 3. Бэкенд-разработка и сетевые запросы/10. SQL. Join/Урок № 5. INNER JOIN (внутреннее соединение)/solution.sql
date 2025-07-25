В базе данных есть две таблицы – клиенты и заказы. Таблицы имеют следующую структуру:

Таблица customers

id	customer_name
1	Kelley Bastie
2	...


Таблица orders

order_id	customer_id	product_name	price
1	            1	        food	    100
2	            2	        computers	1000

Поле customer_id ссылается на поле id таблицы customers


Составьте запрос, который найдет имена клиентов и названия товаров, которые они приобрели. Отсортируйте выборку по имени
клиента в прямом порядке


SELECT
    customer_name,
    product_name
FROM customers
INNER JOIN orders
    ON id = customer_id
ORDER BY customer_name ASC;


SOLUTION

-- IDENTICAL!!!
