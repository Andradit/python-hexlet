"""simple_blog/articles/models.py
Добавьте модель Article с полями:

    - title — CharField с максимальной длиной в 255 символов
    - author — CharField с максимальной длиной в 255 символов

simple_blog/articles/views.py
Измените вью так, чтобы они работали с моделью Article. Вью index() должна все
так же получать все статьи по GET-запросу и добавлять новую по POST-запросу. Вью
article_view() должна получать нужную статью по переданному id.

Сгенерируйте и примените миграции командой make migrate. Запустите репл командой
make console и создайте через него несколько статей. Откройте веб-доступ и
проверьте работу сайта.

Подсказки
    - модели (https://docs.djangoproject.com/en/4.1/topics/db/models/)
    - запросы (https://docs.djangoproject.com/en/4.1/topics/db/queries/)
"""

from django.http import Http404
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from .models import Article


@require_http_methods(['GET', 'POST'])
def index(request):
    # BEGIN (write your solution here)
    articles = Article.objects.all()
    if request.method == "POST":
        Article.objects.create(
            title=request.POST['title'],
            author=request.POST['author']
            )
    # END
    return render(request, 'articles/index.html', context={'articles': articles})


@require_http_methods(['GET'])
def article_view(request, id):
    # BEGIN (write your solution here)
    article = Article.objects.get(pk=id)
    # END
    return render(request, 'articles/article.html', context={'article': article})


'SOLUTION'

# @require_http_methods(['GET', 'POST'])
# def index(request):
# # BEGIN
#     if request.method == 'POST':
#         data = {
#             'title': request.POST['title'],
#             'author': request.POST['author']
#         }
#         Article.objects.create(**data)
#     articles = Article.objects.all()
# # END
#     return render(request, 'articles/index.html', context={'articles': articles})
#
#
# @require_http_methods(['GET'])
# def article_view(request, id):
#     # BEGIN (write your solution here)
#     article = Article.objects.filter(pk=id)[0]
#     print(article)
#     if not article:
#         raise Http404()
#     # END
#     return render(request, 'articles/article.html', context={'article': article})
