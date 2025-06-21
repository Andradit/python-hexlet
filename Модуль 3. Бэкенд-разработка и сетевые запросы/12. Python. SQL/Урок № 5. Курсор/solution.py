"""В практике вам доступны следующие таблицы

    - orders

        - order_id - id заказа
        - customer_id - id покупателя
        - order_date - дата заказа
        - total_amount - сумма заказа

    - customers

        - customer_id - id покупателя
        - customer_name - имя покупателя

Допишите функцию get_order_sum(), которая принимает соединение и месяц, и
возвращает общую сумму заказов каждого покупателя за этот месяц. Функция должна
вернуть результат в виде строки:

Покупатель Emily White совершил покупок на сумму 290
Покупатель John Smith совершил покупок на сумму 130
conn = psycopg2.connect('..')"""

# month = 2
# get_order_sum(conn, month)
# # Покупатель Emily White совершил покупок на сумму 290

import psycopg2
from psycopg2.extras import DictCursor


conn = psycopg2.connect('postgresql://postgres:123456789@localhost:5432/hexlet')
cursor = conn.cursor()

# with open('init.sql', 'r') as file:
#     query = file.read()
#     cursor.execute(query)
#     conn.commit()


# BEGIN (write your solution here)
def get_order_sum(conn, month):
    with conn.cursor(cursor_factory=DictCursor) as curr:
        query = f'''SELECT customers.customer_name, SUM(total_amount) AS total
        FROM orders
        JOIN customers ON orders.customer_id = customers.customer_id
        WHERE EXTRACT(MONTH FROM order_date) = {month}
        GROUP BY customers.customer_name, orders.customer_id
        ORDER BY orders.customer_id;'''
        curr.execute(query)
        record = curr.fetchall()
        result = ''
        for i in record:
            name, total_amount = i[0], i[1]
            result += (f'Покупатель {name} совершил покупок на сумму '
                       f'{total_amount}\n')
        return result.strip()
# END

month = 2
print(get_order_sum(conn, month))
# Покупатель John Smith совершил покупок на сумму 240
# Покупатель Michael Brown совершил покупок на сумму 800

'SOLUTION'

# def get_order_sum(conn, month):
#     template = "Покупатель {customer} совершил покупок на сумму {total}".format
#     with conn.cursor(cursor_factory=DictCursor) as cur:
#         query = """
#             SELECT
#                 c.customer_name,
#                 SUM(o.total_amount) AS total
#             FROM
#                 customers c
#             LEFT JOIN
#                 orders o ON c.customer_id = o.customer_id
#             WHERE
#                 EXTRACT(MONTH FROM o.order_date) = %s
#             GROUP BY
#                 c.customer_name;"""
#         month_formated = '{:02d}'.format(month)
#         cur.execute(query, (month_formated,))
#         result = []
#         for row in cur:
#             customer_name = row['customer_name']
#             total = row['total']
#             result.append(template(customer=customer_name, total=total))
#     conn.commit()
#
#     return '\n'.join(result)
