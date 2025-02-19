Во многих онлайн играх, например в World Of Warcraft, реализована система торговли между пользователями. В этом задании
передадим предмет от одного пользователя другому.

user_items

id	username	item	received_at
1	arya	   Needle	2024-04-19T15:32:01.080Z
2	lord_mormont Longclaw  2024-04-19T15:32:01.080Z
3	lord_mormont The armor of the Nights Watch	2024-04-19T15:32:01.080Z

    - id - первичный ключ
    - username - пользователь
    - item - предмет
    - received_at - дата приобретения предмета

Составьте транзакцию, которая передает предмет Longclaw от пользователя lord_mormont пользователю jon. Передача предмета
выполняется добавлением новой записи в таблицу. При этом все предметы уникальны, а значит они не могут быть у
предыдущего владельца.

Подсказки

В этом задании мы учимся работать с транзакциями, поэтому выполняем два запроса, вместо одного UPDATE.

BEGIN;
DELETE FROM user_items WHERE username = 'lord_mormont' AND item = 'Longclaw';
INSERT INTO user_items (username, item, received_at) VALUES
('jon', 'Longclaw', NOW());
COMMIT;

SOLUTION

-- IDENTICAL!!!