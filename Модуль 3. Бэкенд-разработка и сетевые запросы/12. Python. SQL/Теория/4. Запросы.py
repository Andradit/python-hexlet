import psycopg2
from psycopg2.extras import execute_batch, execute_values

conn = psycopg2.connect('postgresql://postgres:123456789@localhost:5432/hexlet')
cursor = conn.cursor()

name = 'Tota'
phone = '1234'

sql = f"INSERT INTO users (username, phone) VALUES ('{name}', '{phone}');"
cursor.execute(sql)

name = "John"
age = 19

with conn.cursor() as curs:
    # также можно использовать именованные аргументы

    curs.execute(
        "INSERT INTO users (username, age) VALUES (%(name)s, %(age)s);",
        {'age': age, 'name': name})

with conn.cursor() as curs:
    # для позиционных аргументов всегда передается последовательность,
    # даже если параметр один здесь передается кортеж (name,)
    curs.execute("SELECT id, username FROM users WHERE username=%s;",
                 (name,))
    print(curs.fetchall())

with conn.cursor() as curs:
    users = (
        ("Bob", "bob@mail.com"), ("Alice", "alice@mail.com"),
        ("John", "john@mail.com"))
    execute_batch(curs, "INSERT INTO users (username, email) VALUES (%s, %s)",
                  users)

# в случае execute_values запрос будет выглядеть так
# users = [("Bob", "bob@mail.com"), ("Alice", "alice@mail.com"), ("John", "john@mail.com")]
# execute_values(curs, "INSERT INTO users (username, email) VALUES %s", users)


conn.commit()
conn.close()
