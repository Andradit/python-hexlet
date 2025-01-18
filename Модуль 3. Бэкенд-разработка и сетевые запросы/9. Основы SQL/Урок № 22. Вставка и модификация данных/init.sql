DROP TABLE IF EXISTS students_progress;

CREATE TABLE students_progress (
    id bigint GENERATED ALWAYS AS IDENTITY,
    first_name varchar(255),
    last_name varchar(255),
    faculty char(1),
    grade int
);

INSERT INTO students_progress (first_name, last_name, faculty, grade) VALUES
('Andrew', 'Catmull', 'A', 100),
('Silva', 'Rodge', 'B', 95),
('Roseanna', 'Botright', 'C', 80),
('Yorker', 'Fliege', 'C', 19),
('Morganne', 'Folder', 'B', 67),
('Rozelle', 'Bengough', 'A', 12),
('Dorthy', 'Spring', 'B', 10),
('Carry', 'Molnar', 'A', 88),
('Freda', 'Stocks', 'C', 15),
('Sheff', 'Storck', 'C', 70);
