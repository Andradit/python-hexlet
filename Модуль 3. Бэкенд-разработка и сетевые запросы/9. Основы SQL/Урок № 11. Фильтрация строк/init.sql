--noqa: disable=L010, L016
DROP TABLE IF EXISTS users;
CREATE TABLE users (
    id bigint,
    first_name varchar(255),
    last_name varchar(255),
    email varchar(255),
    phone_number varchar(255)
);

INSERT INTO users (id, first_name, last_name, email, phone_number) VALUES
(1, 'Toddie', 'Lamp', 'tlamp0@google.com', '+55-544-156-3886'),
(2, 'Gilli', 'Giannoni', 'ggiannoni1@google.org', null),
(3, 'Kyle', 'Karle', 'kkarle2@squidoo.com', null),
(4, 'Dag', 'Shardlow', 'dshardlow3@github.com', null),
(5, 'Manfred', 'Cano', 'mcano4@google.com', '+689-389-150-8462'),
(6, 'Corette', 'Emmer', 'cemmer5@t-online.de', '+689-123-150-3476'),
(7, 'Mercie', 'Damarell', 'mdamarell6@ow.ly', null),
(8, 'Antonius', 'Swinbourne', 'aswinbourne7@google.com', '+86-965-702-4848'),
(9, 'Madelena', 'Petley', 'mpetley8@biblegateway.com', null),
(10, 'Tuesday', 'Brougham', 'tbrougham9@facebook.com', '+689-389-150-8434');
