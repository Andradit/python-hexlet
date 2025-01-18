Напишите запросы, обновляющие таблицу структуры:

CREATE TABLE users (
    id bigint,
    email varchar(255) NOT NULL,
    age integer,
    name varchar(255)
);

В структуру:

CREATE TABLE users (
    id bigint,
    email varchar(255) NOT NULL UNIQUE,
    first_name varchar(255) NOT NULL,
    created_at timestamp
);

name и first_name - одна и та же колонка.

Подсказки
    - добавление ограничения UNIQUE выполняется через команду ADD
    - установка ограничения NOT NULL выполняется через команды ALTER COLUMN и SET

ALTER TABLE users
ADD UNIQUE (email),
DROP COLUMN age,
ADD COLUMN created_at TIMESTAMP,
ALTER COLUMN name SET NOT NULL;

ALTER TABLE users
RENAME COLUMN name TO first_name;

SOLUTION

-- ALTER TABLE users
-- ADD UNIQUE (email),
-- ADD COLUMN created_at timestamp;
--
-- ALTER TABLE users RENAME COLUMN name TO first_name;
-- ALTER TABLE users DROP COLUMN age;
--
-- ALTER TABLE users ALTER COLUMN first_name SET NOT NULL;