import psycopg2

# Создаем соединение с базой
# hexlet_test - Имя базы данных
try:
    conn = psycopg2.connect(
        'postgresql://postgres:123456789@localhost:5432/hexlet')
except:
    print('Can`t establish connection to database')

sql = ("CREATE TABLE users (id SERIAL PRIMARY KEY, username VARCHAR(255),"
       "phone VARCHAR(255));")
# Запрос выполняется через создание объекта курсора
cursor = conn.cursor()
cursor.execute(sql)
cursor.close()  # в конце закрывается

sql2 = "INSERT INTO users (username, phone) VALUES ('tommy', '123456789');"
cursor = conn.cursor()
cursor.execute(sql2)
cursor.close()

sql3 = "SELECT * FROM users;"
cursor = conn.cursor()
# Указатель на набор данных в памяти СУБД
cursor.execute(sql3)
for row in cursor:
    print(row)
cursor.close()

conn.commit()  # Коммитим, т.е. сохраняем изменения в БД
conn.close()  # Соединение нужно закрыть
