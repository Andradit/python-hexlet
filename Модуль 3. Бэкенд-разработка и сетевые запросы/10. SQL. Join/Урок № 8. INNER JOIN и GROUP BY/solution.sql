В этом упражнении мы посчитаем средний балл студента. В базе данных есть две таблицы – студенты и оценки. Таблицы имеют
следующую структуру:

Таблица students содержит id и имена студентов

student_id	name
1	        Alex Bowman
2	...

Таблица ratings содержит оценки каждого студента по различным предметам (поле name)

id	student_id	name	rating
1	1	        physics	5
2	1	        math	4

Поле ratings.student_id ссылается на поле students.student_id

Составьте запрос, который получит среднюю оценку каждого студента по всем предметам, округленную до десятых. Итоговая
таблица должна иметь поля

    - id - идентификатор студента.
    - student_name - имя студента.
    - average_rating - средняя оценка.

Отсортируйте выборку по среднему баллу студентов в порядке убывания

Подсказки

    - Для округления чисел вам может понадобиться функция ROUND()
    - Используйте псевдонимы, чтобы однозначно определить имена столбцов и не дублировать вычисления


SELECT
    students.student_id AS id,
    students.name AS student_name,
    ROUND(AVG(ratings.rating), 1) AS average_rating
FROM students
INNER JOIN ratings
    ON students.student_id = ratings.student_id
GROUP BY students.student_id, students.name
ORDER BY average_rating DESC;


SOLUTION

-- IDENTICAL!!!