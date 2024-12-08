Составьте запрос, который извлекает из таблицы статей articles названия статей (поле title), у которых поле creator_id
равно 1 или 4.

Подсказки

Структуру таблиц users и articles можно посмотреть в файле init.sql

SELECT title
FROM articles
WHERE creator_id IN (1, 4);

SOLUTION

-- IDENTICAL!!!