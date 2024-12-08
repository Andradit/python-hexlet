--noqa: disable=L010, L016
DROP TABLE IF EXISTS articles, users;

CREATE TABLE users (
    id bigint,
    first_name varchar(255),
    last_name varchar(255)
);

CREATE TABLE articles (
    id bigint,
    title varchar(255),
    content text,
    creator_id bigint
);

INSERT INTO articles (id, title, content, creator_id) VALUES
(1, 'Dialogues with Solzhenitsyn', 'syndicate extensible infomediaries', 2),
(2, 'John Dies at the End', 'grow front-end vortals', 1),
(3, 'Animals are Beautiful People', 'embrace leading-edge paradigms', 3),
(4, 'Hammett', 'matrix rich paradigms', 4),
(5, 'Spy Game', 'enhance cutting-edge applications', 4),
(6, 'Football Factory, The', 'transform synergistic models', 5),
(7, 'Plans for Tomorrow', 'drive sexy solutions', 1),
(8, 'Roman de gare', 'deploy dynamic solutions', 3),
(9, 'Family Law (Derecho de familia)', 'aggregate extensible e-markets', 2),
(10, 'Exists', 'whiteboard impactful action-items', 2);


INSERT INTO users (id, first_name, last_name) VALUES
(1, 'Andrew', 'Lamp'),
(2, 'Gilli', 'Giannoni'),
(3, 'Kyle', 'Karle'),
(4, 'Anna', 'Shardlow'),
(5, 'Manfred', 'Cano');
