Запишите
запросы, которые создают таблицу events и добавляют в нее две записи.

Таблица должна содержать информацию о событиях. В таблице укажите следующие поля:

    - id - идентификатор события
    - name - текстовое поле до 50 символов
    - date - поле с датой проведения
    - time - время проведения
    - location - текстовое поле до 100 символов
    - description - описание события без ограничений

Добавьте в таблицу две записи с любыми данными.


CREATE TABLE events (
    id BIGINT,
    name VARCHAR(50),
    date DATE,
    time TIME,
    location VARCHAR(100),
    description TEXT
);

INSERT INTO events (id, name, date, time, location, description)
VALUES (3, 'Party', '2024-12-25', '18:30:00', 'Moscow', 'Amusements');
INSERT INTO events (id, name, date, time, location, description)
VALUES (8, 'Meeting', '2024-12-30', '19:00:00', 'London', 'Business meeting');


SOLUTION

CREATE TABLE events (
    id INT,
    name VARCHAR(50),
    date DATE,
    time TIME,
    location VARCHAR(100),
    description TEXT
);

INSERT INTO events (
    id,
    name,
    date,
    time,
    location,
    description
) VALUES
(
    1,
    'Birthday Party',
    '2022-03-15',
    '17:00:00',
    '123 Main Street',
    'Join us for a fun-filled birthday celebration!'
),
(
    2,
    'Company Meeting',
    '2022-03-20',
    '09:00:00',
    '456 Business Avenue',
    'Important meeting to discuss company goals and strategies.'
);