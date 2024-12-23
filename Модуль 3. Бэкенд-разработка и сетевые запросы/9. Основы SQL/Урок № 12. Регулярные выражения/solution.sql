В нашей базе данных для каждого сотрудника компании указан внутренний номер телефона. Внутренний номер должен состоять
ровно из трех цифр. В этом упражнении вам предстоит найти всех пользователей, у которых неверно указан внутренний номер
телефона

solution.sql
Составьте запрос, который извлекает из таблицы users имя (поле first_name) и адрес электронной почты (поле email)
пользователей, у которых некорректно указан внутренний номер телефона (поле telephone). Считаем, что правильные номера
телефона содержат три любые цифры, все остальные номера являются некорректными

Подсказки

Эту задачу можно решить разными способами. Для одного из вариантов решения вам может понадобиться квантификатор.
Квантификатор после символа или группы определяет, сколько раз предшествующее выражение может встречаться. Если захотите
немного усложнить задачу, изучите информацию в статье о квантификаторах и попробуйте сделать разные варианты решения – с
квантификатором и без

-- Такое регулярное выражение говорит о том, что в строке может быть ровно две любые буквы латинского алфавита
    '[a-z]{2}'

    'ab'  SIMILAR TO '[a-z]{2}' -- True

-- Тут уже три символа, не подходит
    'ab'  SIMILAR TO '[a-z]{3}' -- False
-- Тут помимо букв есть еще и цифры, не подходит
    'a1'  SIMILAR TO '[a-z]{2}' -- False

SELECT
    first_name,
    email
FROM users
WHERE telephone NOT SIMILAR TO '[0-9]{3}';

SOLUTION

-- IDENTICAL!!!