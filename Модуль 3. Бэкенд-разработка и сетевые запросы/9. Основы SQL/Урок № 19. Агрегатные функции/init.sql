DROP TABLE IF EXISTS staff;

CREATE TABLE staff (
    id BIGINT,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    job_title VARCHAR(255),
    salary INT
);

INSERT INTO staff (id, first_name, last_name, job_title, salary) VALUES
(1, 'Palmer', 'Callf', 'Professor', 1795),
(2, 'Lurline', 'Buncom', 'Librarian', 574),
(3, 'Conroy', 'Meach', 'Geologist', 705),
(4, 'Larina', 'Theodore', 'Professor', 1871),
(5, 'Lindsy', 'Riccetti', 'Engineer', 1994),
(6, 'Tasia', 'Devonshire', 'Librarian', 525),
(7, 'Kylynn', 'Coolson', 'Professor', 840),
(8, 'Hope', 'Romero', 'Geologist', 711),
(9, 'Donovan', 'Smallcomb', 'Librarian', 921),
(10, 'Hurlee', 'Kettlestring', 'Manager', 583),
(11, 'Frasquito', 'Crowdace', 'Director', 1095),
(12, 'Shani', 'Hanselmann', 'Librarian', 1114),
(13, 'Matthiew', 'Houlden', 'Engineer', 1629),
(14, 'Hayyim', 'Bromfield', 'Manager', 891),
(15, 'Aggy', 'Tant', 'Engineer', 1505),
(16, 'Gwyneth', 'Bowater', 'Engineer', 849),
(17, 'Engelbert', 'Dreier', 'Manager', 1934),
(18, 'Pattie', 'Everwin', 'Director', 1341),
(19, 'Hube', 'Myrie', 'Geologist', 863),
(20, 'Theodor', 'Bamlett', 'Geologist', 744);
