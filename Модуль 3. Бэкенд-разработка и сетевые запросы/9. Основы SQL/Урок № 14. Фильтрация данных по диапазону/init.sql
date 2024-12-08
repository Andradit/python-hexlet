--noqa: disable=L010, L016
DROP TABLE IF EXISTS orders;
CREATE TABLE orders (
    id bigint,
    created_at date,
    product varchar(255),
    price int,
    count int,
    buyer varchar(255)
);

INSERT INTO orders (id, created_at, product, price, count, buyer) VALUES
(1, '2022-05-21', 'Cooking book', 100, 2, 'John'),
(2, '2022-07-09', 'BOOK', 10, 1, 'Anna'),
(3, '2022-02-06', 'Bread', 2, 5, 'Jack'),
(4, '2022-07-21', 'Milk', 3, 2, 'Harry'),
(5, '2022-04-23', 'Dress', 20, 1, 'Valery'),
(6, '2022-02-23', 'Harry Potter book', 30, 1, 'Ron'),
(7, '2022-12-18', 'Cheese', 7, 2, 'Patrick'),
(8, '2022-07-12', 'Computer', 1000, 1, 'Joe'),
(10, '2023-01-01', 'my book', 3, 5, 'Hanna');
