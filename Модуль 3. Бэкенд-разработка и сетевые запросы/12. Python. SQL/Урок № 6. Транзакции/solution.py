"""В этом упражнении уже создано соединение с базой данных и следующие таблицы:

posts, которая содержит информацию о постах:

    - id — id поста, первичный ключ, генерируется базой данных автоматически
    - title — название поста
    - content — содержание поста
    - author_id — id автора
    - created_at - дата создания поста, генерируется автоматически

comments, которая содержит информацию о комментариях:

    - id - id комментария, первичный ключ, генерируется базой данных
    автоматически
    - post_id - id поста, к которому оставлен комментарий
    - author_id - id автора
    - content - содержание комментария
    - created_at - дата создания комментария, генерируется автоматически

Реализуйте следующие функции:

create_post() - принимает соединение с базой данных и словарь с данными поста.
Словарь должен содержать ключи: 'title', 'content', 'author_id'. Функция должна
создать новый пост и вернуть его id.

add_comment() - принимает соединение с базой данных и словарь с данными
комментария. Словарь должен содержать ключи: 'post_id', 'author_id', 'content'.
Функция должна добавить новый комментарий и вернуть его id.

get_latest_posts() - принимает соединение с базой данных и количество постов n.
Возвращает список n последних постов с их комментариями. Каждый элемент списка
должен быть словарем с ключами: 'id', 'title', 'content', 'author_id',
'created_at', 'comments'. 'comments' - это список словарей с ключами: 'id',
'author_id', 'content', 'created_at'"""

# conn = psycopg2.connect('..')
#
# get_latest_posts(conn, 1)
# # []
#
# post = {'title': 'My Super Post', 'content': 'text', 'author_id': 42}
# create_post(conn, post) # 1
#
# comment = {'post_id': 1, 'author_id': 42, 'content': 'wow such post'}
# add_comment(conn, comment) # 1
#
# get_latest_posts(conn, 1)
# # [{
# # 'id': 1,
# # 'title': 'My Super Post',
# # 'content': 'text',
# # 'author_id': 42,
# # 'created_at': datetime.datetime(2022, 7, 19, 14, 32, 37, 123857),
# # 'comments': [
# #  {
# #   'id': 1,
# #   'author_id': 42,
# #   'content': 'wow such post',
# #   'created_at': datetime.datetime(2022, 8, 19, 14, 32, 37, 135319)
# #   }
# #  ]}]

import psycopg2
from cloudinit.cmd.status import get_latest_event
from gpg.version import author
from psycopg2.extras import DictCursor
from psycopg2.extras import RealDictCursor

conn = psycopg2.connect('postgresql://postgres:123456789@localhost:5432/hexlet')
cursor = conn.cursor()


# with open('init.sql', 'r') as file:
#     query = file.read()
#     cursor.execute(query)
#     conn.commit()
#
# def create_post(conn, post):
#     values = tuple(post.values())
#     with conn.cursor() as curr:
#         query = ("INSERT INTO posts (title, content, author_id)"
#                  "VALUES (%s, %s, %s) RETURNING id")
#         curr.execute(query, values)
#         user_id = curr.fetchone()[0]
#         conn.commit()
#         return user_id
#
#
# def add_comment(conn, comment):
#     values = tuple(comment.values())
#     with conn.cursor() as curr:
#         query = ("INSERT INTO comments (post_id, author_id, content)"
#                  "VALUES (%s, %s, %s) RETURNING id")
#         curr.execute(query, values)
#         comment_id = curr.fetchone()[0]
#         conn.commit()
#         return comment_id
#
def get_latest_posts(conn, n):
    with conn.cursor(cursor_factory=RealDictCursor) as curr:
        query = f'''SELECT
            p.*,
            c.id as comment_id,
            c.author_id as comment_author_id,
            c.content as comment_content,
            c.created_at as comment_created_at
            FROM posts p JOIN comments c
            ON p.author_id = c.author_id
            ORDER BY p.created_at DESC LIMIT {n};'''
        curr.execute(query)
        # result = curr.fetchall()
        # print(result)

        # post_dict = {}
        # for i in result:
        #     for k, v in i.items():
        #         print(k, v)
        #         post_dict[k] = v
        #         if k == k.startswith('comment_'):
        #             post_dict['comments']: []
        # conn.commit()
        # return post_dict

        rows = curr.fetchall()
        # print(rows)
        posts_dict = {}
        for row in rows:
            post_id = row['id']
            if not posts_dict.get(post_id):
                posts_dict[post_id] = {
                    'id': row['id'],
                    'title': row['title'],
                    'content': row['content'],
                    'author_id': row['author_id'],
                    'created_at': row['created_at'],
                    'comments': []
                }

                if row.get('comment_id'):
                    posts_dict[post_id]['comments'].append({
                        'id': row['comment_id'],
                        'author_id': row['comment_author_id'],
                        'content': row['comment_content'],
                        'created_at': row['comment_created_at']
                    })

            return list(posts_dict.values())


# [
#     {
#         'id': 1,
#         'title': 'My Super Post',
#         'content': 'text',
#         'author_id': 42,
#         'created_at': datetime.datetime(2022, 7, 19, 14, 32, 37, 123857),
#         'comments': [
#             {
#             'id': 1,
#             'author_id': 42,
#             'content': 'wow such post',
#             'created_at': datetime.datetime(2022, 8, 19, 14, 32, 37, 135319)
#             }
#         ]
#     }
# ]


'RealDictCursor'
# [RealDictRow(
#     {'id': 1,
#      'title': 'My Super Post',
#      'content': 'text',
#      'author_id': 42,
#      'created_at': datetime.datetime(2025, 2, 3, 22, 19, 41, 927597),
#      'comment_id': 1,
#      'comment_author_id': 42,
#      'comment_content': 'wow such post',
#      'comment_created_at': datetime.datetime(2025, 2, 3, 22, 19, 41, 929443)
#      }
# )]

'DictCursor'
# [
#     [
#         1,
#         'My Super Post',
#         'text', 42,
#         datetime.datetime(2025, 2, 3, 22, 19, 41, 927597),
#         1,
#         42,
#         'wow such post',
#         datetime.datetime(2025, 2, 3, 22, 19, 41, 929443)
#     ]
# ]

# [
#     [
#         1,
#         'My Super Post',
#         'text',
#         42,
#         datetime.datetime(2025, 2, 3, 22, 19, 41, 927597),
#         1,
#         1,
#         42,
#         'wow such post',
#         datetime.datetime(2025, 2, 3, 22, 19, 41, 929443)
#     ]
# ]


print(get_latest_posts(conn, 1))  # []
#
# post = {'title': 'My Super Post', 'content': 'text', 'author_id': 42}
# create_post(conn, post) # 1
#
# comment = {'post_id': 1, 'author_id': 42, 'content': 'wow such post'}
# add_comment(conn, comment) # 1
#
# print(get_latest_posts(conn, 1))
# [{
# 'id': 1,
# 'title': 'My Super Post',
# 'content': 'text',
# 'author_id': 42,
# 'created_at': datetime.datetime(2022, 7, 19, 14, 32, 37, 123857),
# 'comments': [
#  {
#   'id': 1,
#   'author_id': 42,
#   'content': 'wow such post',
#   'created_at': datetime.datetime(2022, 8, 19, 14, 32, 37, 135319)
#   }
#  ]}]

'SOLUTION'

# BEGIN
# def create_post(conn, post):
#     with conn.cursor() as cur:
#         cur.execute("""
#             INSERT INTO posts (title, content, author_id)
#             VALUES (%(title)s, %(content)s, %(author_id)s)
#             RETURNING id
#         """, post)
#         post_id = cur.fetchone()[0]
#     conn.commit()
#     return post_id
#
#
# def add_comment(conn, comment):
#     with conn.cursor() as cur:
#         cur.execute("""
#             INSERT INTO comments (post_id, author_id, content)
#             VALUES (%(post_id)s, %(author_id)s, %(content)s)
#             RETURNING id
#         """, comment)
#         comment_id = cur.fetchone()[0]
#     conn.commit()
#     return comment_id
#
#
def get_latest_posts(conn, n):
    with conn.cursor(cursor_factory=DictCursor) as cur:
        cur.execute("""
            SELECT
                p.*,
                c.id as comment_id,
                c.author_id as comment_author_id,
                c.content as comment_content,
                c.created_at as comment_created_at
            FROM posts p
            LEFT JOIN comments c ON p.id = c.post_id
            WHERE p.id IN (
                SELECT id FROM posts
                ORDER BY created_at DESC
                LIMIT %s
            )
        """, (n,))

        rows = cur.fetchall()
        print(rows)
        posts_dict = {}
        for row in rows:
            post_id = row['id']
            if not posts_dict.get(post_id):
                posts_dict[post_id] = {
                    'id': row['id'],
                    'title': row['title'],
                    'content': row['content'],
                    'author_id': row['author_id'],
                    'created_at': row['created_at'],
                    'comments': []
                }

            if row.get('comment_id'):
                posts_dict[post_id]['comments'].append({
                    'id': row['comment_id'],
                    'author_id': row['comment_author_id'],
                    'content': row['comment_content'],
                    'created_at': row['comment_created_at']
                })

        return list(posts_dict.values())


# END

# print(get_latest_posts(conn, 1))  # []
#
# post = {'title': 'My Super Post', 'content': 'text', 'author_id': 42}
# create_post(conn, post) # 1
#
# comment = {'post_id': 1, 'author_id': 42, 'content': 'wow such post'}
# add_comment(conn, comment) # 1

# print(get_latest_posts(conn, 1))
# [{
# 'id': 1,
# 'title': 'My Super Post',
# 'content': 'text',
# 'author_id': 42,
# 'created_at': datetime.datetime(2022, 7, 19, 14, 32, 37, 123857),
# 'comments': [
#  {
#   'id': 1,
#   'author_id': 42,
#   'content': 'wow such post',
#   'created_at': datetime.datetime(2022, 8, 19, 14, 32, 37, 135319)
#   }
#  ]}]
