Напишите запрос, создающий таблицу users со следующими полями:

    - username — должно присутствовать
    - email — уникально должно присутствовать
    - created_at — должно присутствовать

Выберите типы данных самостоятельно.

CREATE TABLE users (
    username VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    created_at TIMESTAMP NOT NULL
);

SOLUTION

-- IDENTICAL!!!