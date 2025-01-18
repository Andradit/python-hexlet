Напишите запрос, который извлекает из таблицы заказов orders всех пользователей, которые сделали заказ не менее двух
раз.

Отсортируйте выборку по общей стоимости заказов в порядке убывания. Итоговая выборка должна содержать три поля:

    - buyer_id
    - orders_count
    - total_price
Подсказки

Структуру таблицы orders можно посмотреть в файле init.sql

SELECT
    buyer_id,
    COUNT(product) AS orders_count,
    SUM(price) AS total_price
FROM orders
GROUP BY buyer_id
HAVING COUNT(product) >= 2
ORDER BY total_price DESC;

SOLUTION

-- SELECT
--     buyer_id,
--     COUNT(*) AS orders_count,
--     SUM(price) AS total_price
-- FROM orders
-- GROUP BY buyer_id
-- HAVING COUNT(*) >= 2
-- ORDER BY total_price DESC;