--noqa: disable=L010, L016
DROP TABLE IF EXISTS users;
CREATE TABLE users (
    id bigint,
    first_name varchar(255),
    last_name varchar(255),
    email varchar(255),
    created_at date
);

INSERT INTO users (id, first_name, last_name, email, created_at) VALUES
(1, 'Toddie', 'Lamp', 'tlamp0@google.com', '2022-05-21'),
(2, 'Gilli', 'Giannoni', 'ggiannoni1google.org', '2022-07-09'),
(3, 'Kyle', 'Karle', 'kkarle2@squidoo.com', '2022-02-06'),
(4, 'Dag', 'Shardlow', 'dshardlow3@github', '2022-07-21'),
(5, 'Manfred', 'Cano', 'mcano4@google.com', '2022-04-23'),
(6, 'Corette', 'Emmer', 'cemmer5@t-online.de', '2022-02-23'),
(7, 'Mercie', 'Damarell', 'mdamarell6@ow.ly', '2022-12-18'),
(8, 'Antonius', 'Swinbourne', '7@google.com', '2022-07-12'),
(9, 'Madelena', 'Petley', 'mpetley8@biblegateway.com', '2022-04-13'),
(10, 'Tuesday', 'Brougham', 'tbrougham9@facebook.com', '2022-04-04'),
(11, 'John', 'Smith', 'facebook.com', '2022-01-04'),
(12, 'Sansa', 'Stark', 'facebook.com', '2022-08-01'),
(13, 'Joe', 'Doe', 'facebook.com', '2022-07-01');
