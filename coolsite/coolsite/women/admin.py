from django.contrib import admin
from .models import *

class WomenAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'photo', 'is_published') #Список доп.полей, которые мы хотим видеть в админке
    list_display_links = ('id', 'title') #Поля ссылки
    search_fields = ('title', 'content') #По каким полям можно производить поиск
    list_editable = ('is_published')
    list_filter = ('is_published', 'time_create')

# Register your models here.
admin.site.register(Women, WomenAdmin) #Модель и ее вспомогательный класс

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name') #Список доп.полей, которые мы хотим видеть в админке
    list_display_links = ('id', 'name') #Поля ссылки
    search_fields = ('name',) #По каким полям можно производить поиск КОРТЕЖ, поэтому с одним элементом указана запятая
