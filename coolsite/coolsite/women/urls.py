from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', index, name='home'), #http://127.0.0.1:8000/women/, т.к. women/ определено в основном сщщдышеу urls
    #path('cats/<int:catid>/', categories), #http://127.0.0.1:8000/women/cats/
    #re_path(r'^archive/(?P<year>[0-9]{4})/', archive), #с помощью регулярного выражения
    path('about/', about, name='about'),
    path('addpage/', addpage, name='add_page'),
    path('contact/', contact, name='contact'),
    path('login/', login, name='login'),
    path('post/<int:post_id>', show_post, name='post'),
    path('category/<int:cat_id>', show_category, name='category'),
]