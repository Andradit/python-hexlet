from django.http import HttpResponse
from django.shortcuts import render
from django.views import View


class IndexView(View):
    def get(self, request, *args, **kwargs):
        title = "article"
        return render(request,
                      "articles/index.html",
                      context={"title": title},
                      )

#
# def index(request):
#     title = "article"
#     return render(request,
#                   "articles/index.html",
#                   context={"title": title},
#                   )
