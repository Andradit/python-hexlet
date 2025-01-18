DROP TABLE IF EXISTS users CASCADE;
CREATE TABLE users (
    id bigint,
    email varchar(255) NOT NULL,
    age integer,
    name varchar(255)
);

INSERT INTO users (id, email, age, name) VALUES (1, 'noc@mail.com', 44, 'mike');
