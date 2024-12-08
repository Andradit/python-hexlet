Составьте запрос, который извлекает из таблицы заказов orders имена покупателей (поле buyer), которые приобретали в
магазине книги в 2022 году. Наименование товара находится в поле product, дата заказа — в поле created_at. Товар
считается книгой, если он содержит в своем наименовании подстроку "book" в любом регистре.

Подсказки

    - для решения задачи вам может понадобится функция LOWER(), которая приводит строку к нижнему регистру
    - структуру таблицы orders можно посмотреть в файле init.sql

SELECT buyer
FROM orders
WHERE
    (created_at BETWEEN '2022-01-01' AND '2022-12-31')
    AND product ILIKE '%book%';

SOLUTION

-- SELECT buyer
-- FROM orders
-- WHERE
--     created_at BETWEEN '2022-01-01' AND '2022-12-31'
--     AND LOWER(product) LIKE '%book%';
