Напишите запрос, который создаст таблицу order_details. Таблица должна содержать следующие поля

    - первичный ключ
    - id заказа
    - id товара
    - количество товара

Добавьте в эту таблицу три записи. Структуру других таблиц можно посмотреть в psql или в файле init.sql

Подсказки

Перед тем, как записывать решение в файл, откройте psql и попробуйте сделать выборку там

CREATE TABLE order_details (
    id INTEGER PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    order_id INT,
    product_id INT,
    product_count INT
);

INSERT INTO order_details (order_id, product_id, product_count) VALUES
(1, 1, 3),
(3, 4, 5),
(5, 7, 10);


SOLUTION

-- CREATE TABLE order_details (
--     id INTEGER PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
--     order_id INTEGER,
--     product_id INTEGER,
--     quantity INTEGER
-- );
--
-- INSERT INTO order_details (order_id, product_id, quantity) VALUES
-- (1, 1, 2),
-- (1, 2, 1),
-- (2, 1, 1);