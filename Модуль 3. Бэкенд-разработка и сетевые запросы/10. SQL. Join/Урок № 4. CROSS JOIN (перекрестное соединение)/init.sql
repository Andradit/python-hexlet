DROP TABLE IF EXISTS dishes;
DROP TABLE IF EXISTS drinks;

CREATE TABLE drinks (
    id bigint,
    drink_title varchar(255)
);

CREATE TABLE dishes (
    id bigint,
    dish_title varchar(255)
);

INSERT INTO dishes VALUES
(1, 'Oven-Baked Chili Pork'),
(2, 'Fried Vegetables & Turkey'),
(3, 'Blanched Garlic Venison');

INSERT INTO drinks VALUES
(1, 'Tea'),
(2, 'Coffee'),
(3, 'Juice');
