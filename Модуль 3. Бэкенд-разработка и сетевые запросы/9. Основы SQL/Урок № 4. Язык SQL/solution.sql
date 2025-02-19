В этом задании вам предстоит попрактиковаться в работе с языком SQL – пройти путь от добавления данных в таблицу до их
удаления. Все запросы нужно записывать в файл, указанный в заголовке. Система проверки сама их выполнит внутри базы
данных и проверит результат выполнения.

Запишите в файл следующие три запроса:

  - запрос, который добавляет в таблицу users пользователя Gregory с почтой gregory@google.com
  - запрос, который изменяет адрес электронной почты у пользователя John на johny@hotmail.com
  - запрос, который удаляет из таблицы users пользователя с именем Alex

Подсказки
  - перед тем как записывать решение в файл, откройте консоль REPL и попробуйте выполнить запросы там. После запросов
    попробуйте извлекать информацию из таблицы. Посмотрите, как она изменилась. Не бойтесь сломать что-то в базе,всегда
    можно восстановиться командой make reset в терминале
  - структуру таблицы users можно посмотреть в файле init.sql
  - обратите внимание, что каждый запрос оканчивается точкой с запятой

INSERT INTO users (first_name, email) VALUES
('Gregory', 'gregory@google.com');

UPDATE users SET email = 'johny@hotmail.com' WHERE first_name = 'John';

DELETE FROM users WHERE first_name = 'Alex';