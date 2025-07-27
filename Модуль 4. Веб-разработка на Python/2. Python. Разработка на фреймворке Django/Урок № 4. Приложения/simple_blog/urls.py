"""simple_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

"""simple_blog/urls.py
Свяжите urlpatterns приложений с urlpatterns проекта так, чтобы все пути,
которые начинаются с /articles, перенаправлялись в simple_blog.articles.urls. А
пути, которые начинаются с /categories/, перенаправлялись в
simple_blog.categories.urls. Также назначьте вьюху about в качестве обработчика
маршрута /about/. Она уже реализована в файле simple_blog/views.py.

simple_blog/templates/about.html
Добавьте в шаблон HTML:
    <h1>О блоге</h1>
    <p>Эксперименты с Django на Хекслете</p>

simple_blog/templates/articles.html
Добавьте в шаблон HTML:
    <h1>Статьи</h1>

simple_blog/templates/categories.html
Добавьте в шаблон HTML:
    <h1>Категории статей</h1>

simple_blog/templates/index.html
Добавьте в шаблон ссылки на страницы /articles/, /categories/ и /about/"""

from django.urls import include, path
import views

urlpatterns = [
    path('', views.index),
    # BEGIN (write your solution here)
    path('about/', views.about),
    path("articles/", include("simple_blog.articles.urls")),
    path("categories/", include("simple_blog.categories.urls")),
    # END
]

'SOLUTION'

'IDENTICAL!!!'
