DROP TABLE IF EXISTS students;
DROP TABLE IF EXISTS ratings;

CREATE TABLE students (
    student_id bigint,
    name varchar(255)
);

CREATE TABLE ratings (
    id bigint,
    student_id bigint,
    name varchar(255),
    rating int
);

INSERT INTO students VALUES
(1, 'Jenni Edel'),
(2, 'Tedra Crummay'),
(3, 'Emogene Divis'),
(4, 'Hedvige Hynd'),
(5, 'Coletta Nyland');


INSERT INTO ratings VALUES
(1, 4, 'math', 2),
(2, 1, 'physics', 3),
(3, 5, 'philosophy', 5),
(4, 1, 'philosophy', 5),
(5, 2, 'math', 2),
(6, 2, 'philosophy', 4),
(7, 3, 'math', 5),
(8, 2, 'physics', 3),
(9, 3, 'physics', 4),
(10, 4, 'philosophy', 3),
(11, 4, 'physics', 3),
(12, 5, 'math', 5),
(13, 5, 'physics', 5),
(14, 3, 'philosophy', 5),
(15, 1, 'math', 4);
