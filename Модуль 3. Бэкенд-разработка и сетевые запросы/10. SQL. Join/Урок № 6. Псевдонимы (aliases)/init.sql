DROP TABLE IF EXISTS categories;
DROP TABLE IF EXISTS products;

CREATE TABLE categories (
    id bigint,
    name varchar(255)
);

CREATE TABLE products (
    id bigint,
    category_id bigint,
    name varchar(255)
);

INSERT INTO categories VALUES
(1, 'food'),
(2, 'books'),
(3, 'computers'),
(4, 'mobile phones'),
(5, 'tv'),
(6, 'vehicles');

INSERT INTO products VALUES
(1, 1, 'milk'),
(3, 2, 'Harry Potter'),
(4, 3, 'Acer'),
(5, 3, 'Asus'),
(6, 1, 'juice'),
(7, 5, 'samsung tv'),
(8, 2, 'Crime and Punishment'),
(9, 1, 'apple');
