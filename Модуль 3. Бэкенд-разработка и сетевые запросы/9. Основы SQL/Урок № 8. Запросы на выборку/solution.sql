Составьте запрос, который извлекает из таблицы companies:

    - company_name — названия компаний
    - url — адрес компаний в интернете

Результат должен получиться примерно таким:

company_name	url
'Gigazoom'	'https://mozilla.org'
'Twitterwire'	'http://yahoo.com'


Подсказки
Структуру таблицы companies можно посмотреть в файле init.sql


SELECT company_name,
       url
FROM companies;

SOLUTION

-- IDENTICAL!!!