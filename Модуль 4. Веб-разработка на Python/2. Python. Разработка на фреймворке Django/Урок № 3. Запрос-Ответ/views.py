"""simple_blog/views.py
    - реализуйте вью, которая отвечает за формирование главной страницы /. Вью
    должна использовать шаблон index.html
    - реализуйте вью, которая отвечает за формирование страницы /about. Вью
    должна использовать шаблон about.html
    - реализуйте вью, которая отвечает за формирование страницы /articles. Вью
    должна использовать шаблон layout.html

simple_blog/urls.py
Добавьте два маршрута:

    - /about — использует соответствующую вью
    - /articles — использует соответствующую вью

simple_blog/templates/index.html
Добавьте в шаблон ссылки на страницы /about и /articles.

simple_blog/templates/about.html
Добавьте в шаблон HTML:

    <h1>О блоге</h1>
    <p>Эксперименты с Django на Хекслете</p>

simple_blog/templates/layout.html
Добавьте в шаблон HTML:

    <h1>Статьи</h1>

Подсказки
    - в Django по умолчанию все маршруты должны заканчиваться /. Подробнее об
    этом на странице документации"""

from django.shortcuts import render


# BEGIN (write your solution here)
def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def articles(request):
    return render(request, 'layout.html')


# END

'SOLUTION'

'IDENTICAL!!!'
