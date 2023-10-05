from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404


# Create your views here.
def index(request): #HttpRequest
    return HttpResponse("Страница приложения women.")

def categories(request, catid):
    if(request.GET):
        print(request.GET)
    return HttpResponse(f'<h1>Статьи по категориям.</h1><p>{catid}</p>')

def archive(request, year): #HttpRequest
    if int(year) < 2020:
        #raise Http404()
        return redirect('home', permanent=True) #true - постоянно 301, false - временно 302
    return HttpResponse(f'<h1>Архив по годам.</h1><p>{year}</p>')

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Ой! Страница не найдена.</h1>')