from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404
from .models import *

# Create your views here.

#menu = ["О сайте", "Добавить статью", "Обратная связь", "Войти"]

menu = [
    {'title': 'О сайте', 'url_name': 'about'},
    {'title': 'Добавить статью', 'url_name': 'add_page'},
    {'title': 'Обратная связь', 'url_name': 'contact'},
    {'title': 'Войти', 'url_name': 'login'}
]

def index(request): #HttpRequest
    #return HttpResponse("Страница приложения women.")
    posts = Women.objects.all() #фреймворк сам достает данные
    cats = Category.objects.all()
    #return render(request, 'women/index.html', {'posts': posts, 'menu': menu, 'title': 'Главная страница'}) #Чтобы передать на страницу переменные, передаем в виде словаря
    context = {
        'posts': posts,
        'cats': cats,
        'menu': menu,
        'title': 'Главная страница',
        'cat_selected': 0, #На главной странице отображаются все категории
    }
    return render(request, 'women/index.html', context=context)

def about(request): #HttpRequest
    return render(request, 'women/about.html', {'menu': menu, 'title': 'О сайте'})

def categories(request, catid):
    if(request.POST):
        print(request.POST)
    return HttpResponse(f'<h1>Статьи по категориям.</h1><p>{catid}</p>')

def archive(request, year): #HttpRequest
    if int(year) < 2020:
        #raise Http404()
        return redirect('home', permanent=True) #true - постоянно 301, false - временно 302
    return HttpResponse(f'<h1>Архив по годам.</h1><p>{year}</p>')

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Ой! Страница не найдена.</h1>')

def addpage(request):
    return HttpResponse('Добавить страницу')

def contact(request):
    return HttpResponse('Обратная связь')

def login(request):
    return HttpResponse('Войти')

def show_post(request, post_id):
    return HttpResponse(f'Отображение статьи с id = {post_id}')

def show_category(request, cat_id):
    # HttpResponse(f'Отображение категории с id = {cat_id}')
    posts = Women.objects.filter(cat_id=cat_id)
    cats = Category.objects.all()

    if len(posts) == 0:
        raise Http404()

    context = {
        'posts': posts,
        'cats': cats,
        'menu': menu,
        'title': 'Отображение по рубрикам',
        'cat_selected': 0,  # На главной странице отображаются все категории
    }
    return render(request, 'women/index.html', context=context)
