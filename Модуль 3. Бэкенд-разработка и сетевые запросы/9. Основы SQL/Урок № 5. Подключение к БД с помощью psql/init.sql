CREATE TABLE users (
    user_id INT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    email VARCHAR(100),
    age INT
);

INSERT INTO users (user_id, first_name, last_name, email, age)
VALUES (1, 'Alice', 'Smith', 'alice@example.com', 30);

INSERT INTO users (user_id, first_name, last_name, email, age)
VALUES (2, 'Bob', 'Johnson', 'bob@example.com', 25);

INSERT INTO users (user_id, first_name, last_name, email, age)
VALUES (3, 'Chris', 'Brown', 'chris@example.com', 35);
