Напишите запрос, который найдет в таблице staff максимальную и минимальную зарплату (поле salary) для каждой должности
(поле job_title). Итоговая выборка должна содержать три поля:

    - job_title
    - max_salary
    - min_salary

Выборка должна быть отсортирована по названию должности.

Подсказки

Структуру таблицы staff можно посмотреть в файле init.sql

SELECT
    job_title,
    MAX(salary) AS max_salary,
    MIN(salary) AS min_salary
FROM staff
GROUP BY job_title
ORDER BY job_title;

SOLUTION

-- IDENTICAL!!!