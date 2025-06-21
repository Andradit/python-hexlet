import psycopg2

conn = psycopg2.connect('postgresql://postgres:123456789@localhost:5432/hexlet')
sql = "INSERT INTO users (username, phone) VALUES ('tom', '987456321');"
with conn:
    with conn.cursor() as curs:
        curs.execute(sql)

conn.close()
