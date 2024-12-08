--noqa: disable=L010
DROP TABLE IF EXISTS users;
CREATE TABLE users (
    id bigint,
    first_name varchar(255),
    last_name varchar(255),
    birthday date
);


INSERT INTO users (id, first_name, last_name, birthday) VALUES
(1, 'Winthrop', 'Roony', '2018-05-20'),
(2, 'Marjory', 'Collishaw', '2012-08-13'),
(3, 'Mellie', 'Grunder', '2009-12-10'),
(4, 'Ashely', 'Duffie', '2018-03-07'),
(5, 'Kiel', 'Runciman', '2002-05-25'),
(6, 'Sibby', 'Rankling', '1991-08-13'),
(7, 'Shae', 'Witchell', '2020-04-04'),
(8, 'Leeland', 'Whitnall', '2014-04-23'),
(9, 'Bee', 'Sandell', '1992-09-04'),
(10, 'Niall', 'Cornfoot', '2000-01-01');
