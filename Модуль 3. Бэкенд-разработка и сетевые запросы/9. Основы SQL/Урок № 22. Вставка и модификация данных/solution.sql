В этом упражнении мы поработаем с таблицей успеваемости студентов students_progress. Таблица имеет следующую структуру:

id	first_name	last_name	faculty	grade
1	 Andrew	      Catmull	       A     100
2	...	...	...	...

Идентификатор генерируется автоматически при добавлении новой записи.

1. Добавьте в таблицу успеваемости двух студентов:

    - Oliver Doblin с оценкой 93, который учится на факультете A
    - Perry Fensome с оценкой 54, который учится на факультете B

2. Удалите из таблицы записи о студентах факультета C (поле faculty), у которых низкая успеваемость, то есть оценка в
поле grade ниже 20 баллов

Подсказки

Структуру таблицы students_progress можно посмотреть в файле init.sql

INSERT INTO students_progress (first_name, last_name, faculty, grade) VALUES
('Oliver', 'Doblin', 'A', 93),
('Perry', 'Fensome', 'B', 54);

DELETE FROM students_progress
WHERE faculty = 'C' AND grade < 20;

SOLUTION

-- INSERT INTO students_progress (first_name, last_name, faculty, grade) VALUES
-- ('Oliver', 'Doblin', 'A', 93),
-- ('Perry', 'Fensome', 'B', 54);
--
-- DELETE FROM students_progress
-- WHERE (faculty = 'C' AND grade < 20);