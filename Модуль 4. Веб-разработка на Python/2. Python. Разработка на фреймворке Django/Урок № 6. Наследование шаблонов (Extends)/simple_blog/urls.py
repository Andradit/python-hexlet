from django.urls import include, path
from simple_blog import views

urlpatterns = [
    path('', views.index, name='index'),
    # BEGIN (write your solution here)
    path('about/', views.about, name='about'),
    path('articles/', include("simple_blog.articles.urls"))
    # END
]

'SOLUTION'

'IDENTICAL!!!'
