from django.shortcuts import render, redirect
from django.views.generic.base import View #Импорт базового класса джля всех представлений
from .models import Post, Likes
from .form import CommentsForm

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

class AddComments(View):
    '''Добавление комментария'''
    def post(self, request, pk):
        #print(request.POST)
        #return redirect('/') #после отправки комментария перенаправляем пользователя на главную страницу
        form = CommentsForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False) #если форма валидна, сохраняем в бд. False - приостанавливает сохранение для редактирования или добавления новых данных
            form.post_id = pk
            form.save()
        return redirect(f'/{pk}')

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split('.')[0] #с индексом 0 распарсится ip
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

class AddLike(View):
    def get(self, request, pk):
        ip_client = get_client_ip(request)
        try:
            Likes.objects.get(ip=ip_client, pos_id=pk)
            return redirect(f'/{pk}')
        except:
            new_like = Likes()
            new_like.ip = ip_client
            new_like.pos_id = int(pk)
            new_like.save()
            return redirect(f'/{pk}')

class DelLike(View):
    def get(self, request, pk):
        ip_client = get_client_ip(request)
        try:
            lik = Likes.objects.get(ip=ip_client)
            lik.delete()
            return redirect(f'/{pk}')
        except:
            return redirect(f'/{pk}')
