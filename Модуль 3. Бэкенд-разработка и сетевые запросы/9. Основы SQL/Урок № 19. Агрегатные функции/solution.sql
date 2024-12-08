Напишите запрос, который посчитает среднюю зарплату инженера (Engineer) в компании.

Подсказки

Структуру таблицы staff можно посмотреть в файле init.sql

SELECT AVG(salary)
FROM staff
WHERE job_title = 'Engineer';

SOLUTION

-- IDENTICAL!!!