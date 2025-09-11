from django.shortcuts import render
from django.views.generic.base import TemplateView


class HomePageView(TemplateView):
    template_name = "index.html"

    # Переопределяем поведение метода базового класса TemplateView
    def get_context_data(self, **kwargs):
        # Сначала вызываем базовую реализацию, чтобы получить контекст
        context = super().get_context_data(**kwargs)
        # Добавляем в контекст значение 'World' под ключом 'who'
        context['who'] = 'World'
        # Возвращаем новый контекст
        return context




# def index(request):
#     return render(
#         request,
#         "index.html",
#         context={
#             "who": "World",
#         },
#     )


def about(request):
    tags = ["обучение", "программирование", "python", "oop"]
    return render(
        request,
        "about.html",
        context={"tags": tags},
    )
