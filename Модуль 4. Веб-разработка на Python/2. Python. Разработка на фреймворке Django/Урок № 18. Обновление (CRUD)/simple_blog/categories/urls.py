from django.urls import path
from simple_blog.categories import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='categories_index'),
    path(
        'create/',
        views.CategoryCreateView.as_view(),
        name='categories_create'
    ),
    # BEGIN (write your solution here)
    path("<int:id>/update/", views.CategoryFormEditView.as_view(),
    name="categories_update"),
    # END
    path('<int:id>/', views.CategoryView.as_view(), name='categories_detail'),
]

'SOLUTION'

# BEGIN
# path(
#     '<int:id>/update/',
#     views.CategoryUpdateView.as_view(),
#     name='categories_update'
# ),
# END