"""В этом упражнении нужно реализовать страницу категории, на которой выводится
список статей этой категории.

simple_blog/categories/views.py
Создайте вью, которая извлекает из базы текущую запрошенную категорию по id и
передает ее в шаблон.

Не забудьте подключить вью в categories/urls.py.

simple_blog/templates/categories/index.html
Добавьте ссылку на страницу категории в виде имени каждой категории, например
<a class="link" href="/categories/1">Программирование</a>

simple_blog/templates/categories/category.html
    - выведите имя и описание категории
    - выведите список названий статей категории в виде <ol> списка. Если статей
    в категории нет, то тег <ol> не должен отображаться. Каждое название –
    ссылка на саму статью. Маршрут подсмотрите в файле роутов

simple_blog/templates/articles/article.html
Добавьте ссылку на категорию статьи содержащую имя категории, например
<a href="/categories/1">Программирование</a>

Откройте веб-доступ и проверьте работу сайта.

Подсказки
    - список статей категории можно получить так: category.article_set.all()"""


from django.shortcuts import get_object_or_404, render
from django.views import View
from simple_blog.categories.models import Category


class IndexView(View):

    def get(self, request, *args, **kwargs):
        categories = Category.objects.all()
        return render(request, 'categories/index.html', context={
            'categories': categories,
        })


# BEGIN (write your solution here)
class CategoryView(View):
    def get(self, request, *args, **kwargs):
        category = get_object_or_404(Category, id=kwargs["id"])
        articles = category.article_set.all()
        return render(request, 'categories/category.html', context={
            'category': category, 'articles': articles
        })
# END


'SOLUTION'

'IDENTICAL!!!'
