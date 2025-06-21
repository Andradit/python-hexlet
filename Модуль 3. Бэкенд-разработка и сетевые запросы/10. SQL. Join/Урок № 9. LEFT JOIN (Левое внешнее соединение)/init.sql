DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS orders;
DROP TABLE IF EXISTS products;

CREATE TABLE users (
    id bigint,
    first_name varchar(255),
    last_name varchar(255)
);

CREATE TABLE products (
    id bigint,
    title varchar(255)
);

CREATE TABLE orders (
    id bigint,
    user_id bigint,
    product_id bigint,
    price int,
    created_at date
);

INSERT INTO users VALUES
(1, 'Jenni', 'Edel'),
(2, 'Tedra', 'Crummay'),
(3, 'Marcy', 'Spini'),
(4, 'Emogene', 'Divis'),
(5, 'Hedvige', 'Hynd'),
(6, 'Bernita', 'Spaunton'),
(7, 'Coletta', 'Nyland'),
(8, 'Brnaba', 'Korba');


INSERT INTO products VALUES
(1, 'Orange'),
(2, 'Bread'),
(3, 'Soup'),
(4, 'Mince Meat'),
(5, 'Cake'),
(6, 'Beef'),
(7, 'Ranchero'),
(8, 'Beans'),
(9, 'Juice'),
(10, 'Diet cola');

INSERT INTO orders VALUES
(1, 2, 2, 11, '2022-07-11'),
(2, 5, 5, 12, '2023-04-23'),
(3, 3, 3, 20, '2022-05-07'),
(4, 1, 1, 10, '1998-08-01'),
(5, 7, 4, 35, '2020-09-05'),
(6, 1, 6, 10, '2021-10-15'),
(7, 5, 10, 12, '2022-12-21'),
(8, 2, 7, 11, '2023-01-01'),
(9, 3, 8, 20, '2023-01-01'),
(10, 8, 9, 35, '2019-02-01');
