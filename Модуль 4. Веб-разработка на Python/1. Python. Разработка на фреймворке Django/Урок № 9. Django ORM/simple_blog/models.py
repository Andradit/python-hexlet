"""simple_blog/models.py
Добавьте модель Article с полями:

    - title — CharField с максимальной длиной в 255 символов
    - author — CharField с максимальной длиной в 255 символов
    - created_at — DateTimeField

Добавьте модель Employee с полями:

    - name — CharField с максимальной длиной в 255 символов
    - position — CharField с максимальной длиной в три символа, параметр choices
    выбирает из значений [('TR', 'Trainee'), ('JR', 'Junior'), ('SR', 'Senior'),
    ('CEO', 'CEO')]. По умолчанию задано значение Trainee

Подсказки
    - модели (https://docs.djangoproject.com/en/4.1/topics/db/models/)
    - choices (https://docs.djangoproject.com/en/4.1/ref/models/fields/#choices)
"""

from django.db import models


# BEGIN (write your solution here)
class Article(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)


class Employee(models.Model):
    TRAINEE = 'TR'
    JUNIOR = 'JR'
    SENIOR = 'SR'
    CEO = 'CEO'

    POSITIONS = [
        (TRAINEE, 'Trainee'),
        (JUNIOR, 'Junior'),
        (SENIOR, 'Senior'),
        (CEO, 'CEO'),
    ]

    name = models.CharField(max_length=255)
    position = models.CharField(max_length=3, choices=POSITIONS, default=TRAINEE)

# END


'SOlUTION'

'IDENTICAL!!!'
