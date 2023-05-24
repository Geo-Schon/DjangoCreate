from django.http import HttpResponse
from django.shortcuts import render, reverse
import datetime
import os


def home_view(request):
    template_name = 'app/home.html'
    pages = {
        'Главная страница': reverse('home'),
        'Текущее время': reverse("time"),
        'Содержимое рабочей директории': reverse("workdir")
    }
    context = {'pages': pages}
    return render(request, template_name, context)


def time_view(request):
    current_time = datetime.datetime.now().time()
    responce = f'Текущее время: {current_time}'
    return HttpResponse(responce)


def workdir_view(request):
    list_work = []
    path = '.'
    results = os.listdir(path)
    for res in results:
        list_work.append(f'{res}, ')
    return HttpResponse(list_work)
