В этом упражнении мы продолжим работать с интернет-магазином. У нас есть три таблицы. Таблицы имеют следующую структуру:

Таблица users хранит информацию о пользователях

id	first_name	last_name
1	Alex	    Bowman
2	...

Таблица products хранит информацию о товарах магазина

id	title
1	Bread
2	...

Таблица orders хранит информацию о сделанных заказах

id	user_id	product_id	price	created_at
1	1	    2	        5	    2022-10-12

Составьте запрос, который получит имена и фамилии всех пользователей, а также идентификаторы сделанных ими заказов.
Выборку отсортируйте по фамилии и идентификатору заказа в прямом порядке. Выборка должна содержать всех пользователей,
даже если они не сделали ни одного заказа. Итоговая таблица должна содержать поля first_name, last_name и order_id


SELECT
    users.first_name,
    users.last_name,
    orders.id AS order_id
FROM users
LEFT JOIN orders ON users.id = orders.user_id
ORDER BY users.last_name, orders.id;


SOLUTION

-- IDENTICAL!!!