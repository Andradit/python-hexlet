import psycopg2
from psycopg2.extras import NamedTupleCursor, RealDictCursor, DictCursor
from tdb import INSERT

conn = psycopg2.connect('postgresql://postgres:123456789@localhost:5432/hexlet')
cursor = conn.cursor()

with conn.cursor() as curs:
    curs.execute('SELECT * FROM users;')
    all_users = curs.fetchall()
    for row in all_users:
        print(row)

# name = "Alfred"
# age = 90
#
# with conn.cursor() as curs:
#     curs.execute(
#         "INSERT INTO users (username, age) VALUES (%(name)s, %(age)s);",
#         {'age': age, 'name': name})


with conn.cursor(cursor_factory=NamedTupleCursor) as curs:
    curs.execute('SELECT * FROM users WHERE username=%s;',
                 ('Alfred',))
    alfred = curs.fetchone()
    print(alfred)  # Record(id=9, username='Alfred', phone=None, age=90, email=None)
    print(tuple(alfred))  # (9, 'Alfred', None, 90, None)

with conn.cursor(cursor_factory=RealDictCursor) as curs:
    curs.execute('SELECT * FROM users WHERE username=%s;',
                 ('Alfred',))
    alfred = curs.fetchone()
    print(alfred)  # RealDictRow({'id': 9, 'username': 'Alfred', 'phone': None, 'age': 90, 'email': None})
    print(dict(alfred))  # {'id': 9, 'username': 'Alfred', 'phone': None, 'age': 90, 'email': None}

with conn.cursor(cursor_factory=DictCursor) as curs:
    curs.execute('SELECT * FROM users WHERE username=%s;',
                 ('Alfred',))
    alfred = curs.fetchone()
    print(alfred)  # [9, 'Alfred', None, 90, None]
    print(dict(alfred))  # {'id': 9, 'username': 'Alfred', 'phone': None, 'age': 90, 'email': None}

with conn.cursor(cursor_factory=NamedTupleCursor) as curs:
    curs.execute('SELECT MAX(id) from users')
    max_id = curs.fetchone()
    print(max_id)  # Record(max=9)
    print(tuple(max_id))  # (9,)


conn.commit()
conn.close()
