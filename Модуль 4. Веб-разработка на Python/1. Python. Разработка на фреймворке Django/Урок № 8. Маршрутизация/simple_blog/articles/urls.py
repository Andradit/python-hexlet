from django.urls import path
from simple_blog.articles import views


urlpatterns = [
    path('', views.index),
    # BEGIN (write your solution here)
    path('<int:article_id>/', views.get_article),
    # END
]

'SOLUTION'

'IDENTICAL!!!'
