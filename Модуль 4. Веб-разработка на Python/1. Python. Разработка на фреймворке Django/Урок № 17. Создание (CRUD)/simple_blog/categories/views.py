"""simple_blog/categories/urls.py
Добавьте маршрут для создания категории.

simple_blog/categories/views.py
Реализуйте следующие обработчики маршрутов:

    - GET /categories/create/ — страница создания категории
    - POST /categories/create/ — создание новой категории

simple_blog/templates/categories/index.html
Добавьте ссылку на создание категории.

simple_blog/categories/forms.py
Реализуйте форму для создания категории. Добавьте следующие валидации:

    - имя (name) — обязательно и должно быть максимум 100 знаков
    - описание (description) — обязательно и должно быть максимум 200 знаков
    - состояние (state) — может быть либо draft, либо published

simple_blog/templates/categories/create.html
Реализуйте шаблон для создания категории. Добавьте три поля:

    - name
    - description
    - state

Добавьте вывод ошибок.

Подсказки
Создание форм из моделей
(https://docs.djangoproject.com/en/5.2/topics/forms/modelforms/#modelform)"""


from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from simple_blog.categories.models import Category
# BEGIN (write your solution here)
from django.urls import reverse
from simple_blog.categories.forms import CategoryForm
# END


class IndexView(View):

    def get(self, request, *args, **kwargs):
        categories = Category.objects.all()
        return render(request, 'categories/index.html', context={
            'categories': categories,
        })


class CategoryView(View):

    def get(self, request, *args, **kwargs):
        category = get_object_or_404(Category, id=kwargs['id'])
        return render(request, 'categories/category.html', context={
            'category': category,
        })


# BEGIN (write your solution here)
class CategoryCreateView(View):
    def get(self, request, *args, **kwargs):
        form = CategoryForm()
        return render(request, 'categories/create.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('categories_index'))
        return render(request, 'categories/create.html', {'form': form})
# END

'SOLUTION'

'IDENTICAL!!!'