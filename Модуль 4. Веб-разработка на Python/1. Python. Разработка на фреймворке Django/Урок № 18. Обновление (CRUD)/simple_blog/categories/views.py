"""simple_blog/categories/urls.py
Добавьте маршрут для редактирования категории.

simple_blog/categories/views.py
Реализуйте следующие обработчики маршрутов:

    - GET /categories/<int:id>/update/ — страница редактирования категории
    - POST /categories/<int:id>/update/ — обновление категории

simple_blog/templates/categories/index.html
Добавьте ссылку на редактирование категории.

simple_blog/templates/categories/update.html
Добавьте ссылку оправку формы по типу <form action="" method="post">"""


from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from simple_blog.categories.models import Category
from simple_blog.categories.forms import CategoryForm


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


class CategoryCreateView(View):

    def get(self, request, *args, **kwargs):
        form = CategoryForm()
        return render(request, 'categories/create.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categories_index')

        return render(request, 'categories/create.html', {'form': form})


# BEGIN (write your solution here)
class CategoryFormEditView(View):
    def get(self, request, *args, **kwargs):
        category_id = kwargs.get("id")
        category = Category.objects.get(id=category_id)
        form = CategoryForm(instance=category)
        return render(
            request, "categories/update.html", {"form": form,
            "category_id": category_id}
        )

    def post(self, request, *args, **kwargs):
        category_id = kwargs.get("id")
        category = Category.objects.get(id=category_id)
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect("categories_index")

        return render(
            request, "categories/update.html", {"form": form,
            "category_id": category_id}
        )
# END


'SOLUTION'

# BEGIN
# class CategoryUpdateView(View):
#
#     def get(self, request, *args, **kwargs):
#         category_id = kwargs.get('id')
#         category = Category.objects.get(id=category_id)
#         form = CategoryForm(instance=category)
#         return render(request, 'categories/update.html', {
#             'form': form,
#             'category_id': category_id
#             }
#         )
#
#     def post(self, request, *args, **kwargs):
#         category_id = kwargs.get('id')
#         category = Category.objects.get(id=category_id)
#         form = CategoryForm(request.POST, instance=category)
#         if form.is_valid():
#             form.save()
#             return redirect('categories_index')
#
#         return render(request, 'categories/update.html', {
#             'form': form,
#             'category_id': category_id
#             }
#         )
# END

