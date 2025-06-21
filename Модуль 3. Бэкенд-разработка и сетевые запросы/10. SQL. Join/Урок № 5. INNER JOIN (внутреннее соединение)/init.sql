DROP TABLE IF EXISTS categories;
DROP TABLE IF EXISTS products;

CREATE TABLE customers (
    id bigint,
    customer_name varchar(255)
);

CREATE TABLE orders (
    order_id bigint,
    customer_id bigint,
    product_name varchar(255),
    price int
);

INSERT INTO customers VALUES
(1, 'Kelley Bastie'),
(2, 'Darcy Pinkard'),
(3, 'Ludovika Maiklem'),
(4, 'Adriaens Bottrill'),
(5, 'Else Menelaws'),
(6, 'Kinnie Kearney');


INSERT INTO orders VALUES
(1, 1, 'Milk', 50),
(2, 2, 'Mobile phone', 5000),
(3, 5, 'Harry Potter book', 500),
(4, 4, 'Computer', 20000),
(5, 3, 'Tv', 15000);
