from django.shortcuts import render
from django.views.generic.base import View #Импорт базового класса джля всех представлений
from .models import Post

# Create your views here.
class PostView(View):
    '''Вывод записей'''
    def get(self, request): #передаем информацию от пользователя
        posts = Post.objects.all() #все заголовки в переменную помещаем
        return render(request, 'blog/blog.html', {'post_list': posts}) #объединяет указанный шаблон со словарем

class PostDetail(View):
    '''Отдельная страница записи'''
    def get(self, request, pk):
        post = Post.objects.get(id=pk)
        return render(request, 'blog/blog_detail.html', {'post': post})