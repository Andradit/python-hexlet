"""
URL configuration for hexlet_django_blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include  # <- добавлен include
from django.views.generic import TemplateView

from hexlet_django_blog import views
from hexlet_django_blog.views import HomePageView

urlpatterns = [
    path('', HomePageView.as_view()),  # <- добавляем эту строчку
    path("articles/", include("hexlet_django_blog.article.urls")),
    # новая строчка
    path("about/", views.about),  # <- добавляем эту строчку
    path("admin/", admin.site.urls),
]
