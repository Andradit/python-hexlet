"""В этой практике вам предстоит создать обработчик приложения categoies,
выводящий список категорий и подключить его к основному приложению.

simple_blog/urls.py
Реализуйте маршрут /categories и свяжите его с index маршрутом в
simple_blog/categories/urls.py.

simple_blog/categories/urls.py
Создайте маршрут для индексовой страницы. Сделайте маршрут именованным.

simple_blog/categories/views.py
Создайте вью. Извлеките из базы все категории и передайте их в шаблон
templates/categories/index.html.

simple_blog/templates/categories/index.html
Выведите категории любым удобным способом. Для каждой категории нужно вывести ее
название 'name' и описание 'description'.

simple_blog/templates/navigation.html
Добавьте ссылку, которая ведет на страницу категорий. Используйте тег {% url %}.
"""

from django.shortcuts import render
from django.views import View
from simple_blog.categories.models import Category


# BEGIN (write your solution here)
class IndexView(View):
    def get(self, request, *args, **kwargs):
        categories = Category.objects.all()
        return render(
            request,
            "categories/index.html",
            context={
                "categories": categories,
            },
        )


# END

'SOLUTION'

'IDENTICAL!!!'
