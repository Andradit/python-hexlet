"""В этом упражнении уже создано соединение с базой данных и таблица movies,
которая содержит информацию о фильмах. Таблица содержит следующие поля:

    - id — идентификатор фильма, первичный ключ, генерируется базой данных
    автоматически
    - title — название фильма
    - release_year — год выпуска на экран
    - duration — длительность фильма в минутах

Напишите функцию add_movies(). Функция принимает соединение с БД и должна
добавить в таблицу movies два фильма:

    - 'Godfather' длительностью 175 минут, выпущенный в 1972 году
    - 'The Green Mile' длительностью 189 минут, выпущенный в 1999 году

Напишите также функцию get_all_movies(). Функция принимает соединение с БД и
должна получить список всех фильмов, которые содержатся в базе данных в таблице
movies. Каждый фильм — это новая строка формата Godfather 1972 175."""

# conn = psycopg2.connect('..')
#
# get_all_movies(conn)
# # [(1, 'The Dark Knight', 2008, 152),
# # (2, '12 Angry Men', 1957, 96),
# # (3, 'Pulp Fiction', 1994, 154)]
#
# add_movies(conn)
#
# get_all_movies(conn)
# # [(1, 'The Dark Knight', 2008, 152),
# # (2, '12 Angry Men', 1957, 96),
# # (3, 'Pulp Fiction', 1994, 154),
# # (4, 'Godfather', 1972, 175),
# # (5, 'The Green Mile', 1999, 189)]

import psycopg2

conn = psycopg2.connect('postgresql://tirion:secret@localhost:5432/tirion')


def add_movies(conn):
    sql = """INSERT INTO movies (title, release_year, duration)
    VALUES ('Godfather', '1972', '175'), ('The Green Mile', '1999', '189');"""
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()


def get_all_movies(conn):
    sql = "SELECT * FROM movies;"
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    return list(cursor)


'ALTERNATIVE SOLUTION'


def add_movies(conn):
    films = [
        ('Godfather', '1972', '175'),
        ('The Green Mile', '1999', '189')
    ]
    film_records = ", ".join(["%s"] * len(films))
    insert_query = (f"INSERT INTO movies (title, release_year, duration)"
                    f"VALUES {film_records};")
    cursor = conn.cursor()
    cursor.execute(insert_query, films)
    conn.commit()


#
#
# def get_all_movies(conn):
#     insert_query = (f"SELECT id, title, release_year, duration FROM movies")
#     cursor = conn.cursor()
#     cursor.execute(insert_query)
#     conn.commit()
#     return list(cursor)

'SOLUTION'

# def add_movies(conn):
#     curs = conn.cursor()
#     sql = """ INSERT INTO movies (title, release_year, duration)
#     VALUES ('Godfather', 1972, 175), ('The Green Mile', 1999, 189);"""
#     curs.execute(sql)
#     conn.commit()
#
#
# def get_all_movies(conn):
#     curs = conn.cursor()
#     sql = "SELECT * FROM movies;"
#     curs.execute(sql)
#     conn.commit()
#     return list(curs)
