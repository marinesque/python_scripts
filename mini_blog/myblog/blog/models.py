from django.db import models
from datetime import datetime

# Create your models here.
class Post(models.Model):
    '''Данные о записи'''
    title = models.CharField('Заголовок записи', max_length=100) #атрибут - строка из n символов
    description = models.TextField('Текст записи')
    author = models.CharField('Имя автора', max_length=100)
    date = models.DateField('Дата публикации', default=datetime.now)
    img = models.ImageField('Изображение', upload_to='image/%Y', default='/image/noimage.png')

    def __str__(self):
        return f'{self.title}, {self.author}'  # удобный метод для вывода информации об авторе топика

    class Meta:
        verbose_name = 'Запись' #для удобно читаемого имени модели
        verbose_name_plural = 'Записи'

class Comments(models.Model):
    '''Комментарий'''
    email = models.EmailField()
    name = models.CharField('Имя', max_length=50)
    text_comments = models.TextField('Текст комментария', max_length=2000)
    post = models.ForeignKey(Post, verbose_name='Публикация', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}, {self.post}'  # удобный метод для вывода информации о комментаторе

    class Meta:
        verbose_name = 'Комментарий' #для удобно читаемого имени модели
        verbose_name_plural = 'Комментарии'