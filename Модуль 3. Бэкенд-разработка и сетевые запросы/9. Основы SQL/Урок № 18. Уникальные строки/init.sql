--noqa: disable=L010, L016
DROP TABLE IF EXISTS orders;
CREATE TABLE orders (
    id bigint,
    created_at date,
    product varchar(255),
    price int,
    buyer varchar(255)
);

INSERT INTO orders (id, created_at, product, price, buyer) VALUES
(1, '2022-05-21', 'book', 20, 'John'),
(2, '2022-07-09', 'book', 10, 'Anna'),
(3, '2022-02-06', 'cellphone', 100, 'Jack'),
(4, '2022-07-21', 'milk', 3, 'Harry'),
(5, '2022-04-23', 'dress', 20, 'Valery'),
(6, '2022-02-23', 'computer', 300, 'Ron'),
(7, '2022-12-18', 'computer', 500, 'Patrick'),
(8, '2022-07-12', 'book', 30, 'Joe'),
(10, '2023-01-01', 'dress', 3, 'Hanna'),
(11, '2023-01-02', 'dress', 7, 'Hanna');
