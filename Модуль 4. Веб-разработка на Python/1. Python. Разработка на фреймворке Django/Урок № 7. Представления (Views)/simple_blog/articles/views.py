"""simple_blog/articles/views.py
Создайте view function, которая выводит список статей в приложении articles по
пути /articles/.

Функция должна:

    - выводить список всех статей из переменной articles по методу GET. Для
    этого передавайте переменную в контексте по ключу 'articles' и используйте
    шаблон layout.html
    - добавлять статью в список по методу POST. Для этого получайте значения по
    ключам title и author из request.POST. После этого выводите список всех
    статей
    - отдавать ошибку 405 на другие методы. Для этого используйте декоратор
    @require_http_methods

Не забудьте подключить вью в articles/urls.py.

Подсказки
    - функция render()
    - request.POST
    - @require_http_methods
    - вы можете проверить POST-запросы через curl в терминале практики,
    отправляя запросы по localhost:8080/articles. Для этого вью обернута в
    декоратор @csrf_exempt, который позволяет отправлять POST-запросы обходя
    csrf-защиту. Разумеется это сделано в обучающих целях и в реальной
    разработке использовать этот декоратор опасно."""

from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt


articles = [
    {'title': '"How to foo?"', 'author': 'F. BarBaz'},
    {'title': '"Force 101"', 'author': 'O-W. Kenobi'},
    {'title': '"Top 10 skyscrapers"', 'author': 'K. Kong'},
    {'title': '"Top 10 skyscrapers (jp. edition)"', 'author': 'K. Godzilla'},
    {'title': '"5 min recepies"', 'author': 'H. Lector'},
]


@csrf_exempt
# BEGIN (write your solution here)
@require_http_methods(["GET", "POST"])
def index(request):
    if request.method == "GET":
        return render(
            request, "layout.html", context={'articles': articles}
        )
    elif request.method == "POST":
        article = {
            'title': request.POST['title'],
            'author': request.POST['author']
        }
        articles.append(article)
        return render(
            request, "layout.html", context={'articles': articles}
        )
# END


'SOLUTION'

# BEGIN
# @require_http_methods(['GET', 'POST'])
# def index(request):
#     if request.method == 'POST':
#         article = {
#             'title': request.POST['title'],
#             'author': request.POST['author']
#         }
#         articles.append(article)
#     return render(request, 'layout.html', context={'articles': articles})
# END
