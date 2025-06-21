Это задание не связано напрямую с темой урока. Но будет не лишним еще раз попрактиковаться в создании таблиц и вставке
данных

solution.sql
Создайте таблицу users со следующими полями:

    - id - идентификатор пользователя
    - name - имя пользователя

Добавьте в таблицу users одну запись с именем пользователя Tom.

Создайте таблицу cars со следующими полями:

    - id - идентификатор автомобиля
    - user_id - при вставке записи здесь указывается идентификатор пользователя - владельца автомобиля из таблицы users
    - model - Модель автомобиля

Добавьте в таблицу cars два автомобиля любой марки, принадлежащие созданному ранее пользователю

Подсказки

Перед тем как писать запросы в файл, зайдите в psql и поэкспериментируйте

--noqa: disable=L010
-- BEGIN (write your solution here)
CREATE TABLE users (
    id INTEGER,
    name TEXT
);

INSERT INTO users (id, name) VALUES (1, 'Tom');


CREATE TABLE cars (
    car_id INTEGER,
    user_id INTEGER,
    model TEXT
);

INSERT INTO cars (car_id, user_id, model) VALUES
(1, 1, 'Honda'),
(2, 5, 'BMW');
-- END

SOLUTION

-- CREATE TABLE users (
--     id bigint,
--     name varchar(255)
-- );
--
-- CREATE TABLE cars (
--     id bigint,
--     user_id bigint,
--     model varchar(255)
-- );
--
--
-- INSERT INTO users VALUES (1, 'Tom');
--
-- INSERT INTO cars VALUES
-- (1, 1, 'Bmw'),
-- (2, 1, 'Audi');