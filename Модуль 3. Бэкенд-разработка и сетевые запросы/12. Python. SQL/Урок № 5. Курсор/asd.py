dictionary = {
    "foo": "bar",
    "baz": 42,
    "items": 3
}

print(tuple(dictionary.values()))

import json
from psycopg2.extras import RealDictCursor


def create_post(conn, post):
    values = tuple(post.values())
    with conn.cursor() as curr:
        query = "INSERT INTO posts (title, content, author_id) VALUES (%s, %s, %s) RETURNING id"
        curr.execute(query, values)
        user_id = curr.fetchone()[0]
        conn.commit()
        return user_id


def add_comment(conn, comment):
    values = tuple(comment.values())
    with conn.cursor() as curr:
        query = "INSERT INTO comments (post_id, author_id, content) VALUES (%s, %s, %s) RETURNING id"
        curr.execute(query, values)
        comment_id = curr.fetchone()[0]
        conn.commit()
        return comment_id


def get_latest_posts(conn, n):
    with conn.cursor(cursor_factory=RealDictCursor) as curr:
        query = f'SELECT * FROM posts JOIN comments ON posts.author_id = comments.author_id ORDER BY posts.created_at DESC LIMIT %s'
        curr.execute(query)
        result = curr.fetchall()
        conn.commit()
        return result
