--noqa: disable=L010
DROP TABLE IF EXISTS companies;
CREATE TABLE companies (
    id bigint,
    company_name varchar(255),
    phone varchar(255),
    url varchar(255)
);

INSERT INTO companies (id, company_name, phone, url) VALUES
(1, 'Gigazoom', '+389 (420) 676-1326', 'https://mozilla.org'),
(2, 'Twitterwire', '+970 (678) 891-4269', 'http://yahoo.com'),
(3, 'Cogibox', '+81 (315) 592-1839', 'http://sakura.ne.jp'),
(4, 'Twinder', '+370 (916) 707-7594', 'http://hostgator.com'),
(5, 'Vimbo', '+62 (237) 990-4645', 'http://xing.com');
