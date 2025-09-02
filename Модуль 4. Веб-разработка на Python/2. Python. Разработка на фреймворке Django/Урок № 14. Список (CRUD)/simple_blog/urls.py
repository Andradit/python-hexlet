from django.urls import include, path
from simple_blog import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('articles/', include('simple_blog.articles.urls')),
    # BEGIN (write your solution here)
    path('categories/', include('simple_blog.categories.urls'))
    # END
]

'SOLUTION'

'IDENTICAL!!!'
