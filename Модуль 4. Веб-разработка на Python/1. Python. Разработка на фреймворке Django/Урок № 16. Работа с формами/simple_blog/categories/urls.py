from django.urls import path
from simple_blog.categories import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='categories_index'),
    # BEGIN (write your solution here)
    path('<int:id>/', views.CategoryView.as_view(), name='category_detail'),
    # path('categories/<int:id>/', views.CategoryView.as_view(), name='category'),
    # END
]

'SOLUTION'

# BEGIN
# path('<int:id>/', views.CategoryView.as_view(), name='categories_detail'),
# END
