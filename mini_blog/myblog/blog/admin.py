from django.contrib import admin
from .models import Post, Comments
# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author') #отвечает за заголовки записей

@admin.register(Comments)
class PostAdmin(admin.ModelAdmin):
    list_display = ('name', 'post')