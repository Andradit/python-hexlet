Составьте запрос, который извлекает из таблицы персонала staff данные о сотрудниках отдела продаж (значение sales в поле
department):

    - имя (поле first_name)
    - фамилия (поле last_name)
    - зарплата (поле salary)

Данные должны быть отсортированы по полю first_name по возрастанию и в обратном порядке (по убыванию) по полю salary

Подсказки

Структуру таблицы можно посмотреть в файле init.sql

SELECT
    first_name,
    last_name,
    salary
FROM staff
WHERE department = 'sales'
ORDER BY first_name ASC, salary DESC;


SOLUTION

-- IDENTICAL!!!