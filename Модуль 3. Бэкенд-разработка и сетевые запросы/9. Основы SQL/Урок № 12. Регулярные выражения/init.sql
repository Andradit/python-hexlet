--noqa: disable=L010, L016
DROP TABLE IF EXISTS users;
CREATE TABLE users (
    id bigint,
    first_name varchar(255),
    last_name varchar(255),
    email varchar(255),
    telephone varchar(255)
);

INSERT INTO users (id, first_name, last_name, email, telephone) VALUES
(1, 'Toddie', 'Lamp', 'tlamp0@google.com', '197'),
(2, 'Gilli', 'Giannoni', 'ggiannoni1@google.org', '934'),
(3, 'Kyle', 'Karle', 'kkarle2@squidoo.com', '045'),
(4, 'Dag', 'Shardlow', 'dshardlow3@github.com', '19'),
(5, 'Manfred', 'Cano', 'mcano4@google.com', '995'),
(6, 'Corette', 'Emmer', 'cemmer5@t-online.de', '99541'),
(7, 'Mercie', 'Damarell', 'mdamarell6@ow.ly', '381'),
(8, 'Antonius', 'Swinbourne', 'aswinbourne7@google.com', '90r');
