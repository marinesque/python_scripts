from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request): #HttpRequest
    return HttpResponse("Страница приложения women.")

def categories(request, catid):
    return HttpResponse(f'<h1>Статьи по категориям.</h1><p>{catid}</p>')