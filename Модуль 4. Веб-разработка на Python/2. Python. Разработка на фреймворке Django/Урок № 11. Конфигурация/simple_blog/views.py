from django.shortcuts import render
from django.conf import settings


def index(request):
    return render(
        request,
        'index.html',
        context={
            'username': settings.USERNAME,
            'password': settings.PASSWORD,
            }
    )


def about(request):
    return render(request, 'about.html')
