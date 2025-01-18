--noqa: disable=L010, L016
DROP TABLE IF EXISTS orders;
CREATE TABLE orders (
    id bigint,
    created_at date,
    product varchar(255),
    price int,
    buyer_id int
);

INSERT INTO orders (id, created_at, product, price, buyer_id) VALUES
(1, '2022-05-21', 'book', 20, 1),
(2, '2022-07-09', 'book', 10, 2),
(3, '2022-02-06', 'cellphone', 100, 3),
(4, '2022-07-21', 'milk', 3, 4),
(5, '2022-04-23', 'dress', 20, 5),
(6, '2022-02-23', 'computer', 300, 1),
(7, '2022-12-18', 'computer', 500, 1),
(8, '2022-07-12', 'book', 30, 3),
(10, '2023-01-01', 'dress', 3, 1),
(11, '2023-01-02', 'dress', 7, 5);
