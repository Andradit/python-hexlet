DROP TABLE IF EXISTS students;
DROP TABLE IF EXISTS course_members;

CREATE TABLE students (
    student_id bigint,
    first_name varchar(255),
    last_name varchar(255)
);

CREATE TABLE course_members (
    id bigint,
    student_id bigint,
    course_name varchar(255)
);

INSERT INTO students VALUES
(1, 'Jenni', 'Edel'),
(2, 'Tedra', 'Crummay'),
(3, 'Emogene', 'Divis'),
(4, 'Hedvige', 'Hynd'),
(5, 'Coletta', 'Nyland');


INSERT INTO course_members VALUES
(1, 4, 'math'),
(2, 1, 'physics'),
(3, 5, 'philosophy'),
(4, 2, 'math'),
(5, 2, 'philosophy'),
(6, 3, 'math'),
(7, 2, 'physics'),
(9, 5, 'math'),
(10, 5, 'physics'),
(11, 1, 'math');
