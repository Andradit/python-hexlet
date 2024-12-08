DROP TABLE IF EXISTS staff;

CREATE TABLE staff (
    id bigint,
    first_name varchar(255),
    last_name varchar(255),
    department varchar(255),
    salary int
);

INSERT INTO staff (id, first_name, last_name, department, salary) VALUES
(1, 'Gregor', 'Proske', 'construction', 1500),
(2, 'Maggy', 'Colville', 'sales', 1000),
(3, 'Caren', 'Codd', 'investigation', 1200),
(4, 'Maurine', 'Handling', 'engineering', 800),
(5, 'Peg', 'Brewitt', 'engineering', 950),
(6, 'Hadleigh', 'Meddick', 'sales', 1500),
(7, 'Guntar', 'Trapp', 'engineering', 1000),
(8, 'Kyrstin', 'MacShirrie', 'investigation', 9000),
(9, 'Kippie', 'Gerauld', 'investigation', 1200),
(10, 'Lars', 'Hallibone', 'construction', 1500),
(11, 'Melodee', 'Bagshawe', 'sales', 950),
(12, 'Goldarina', 'Bloomfield', 'construction', 2000),
(13, 'Kimbra', 'Hansom', 'support', 600),
(14, 'Anatol', 'Arrundale', 'support', 600),
(15, 'Elise', 'Rattray', 'investigation', 1100),
(16, 'Maggy', 'Ratt', 'sales', 1300);
