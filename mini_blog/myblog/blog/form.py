from django import forms
from .models import Comments

class CommentsForm(forms.ModelForm): #связываем модель комментариев с полученной с блога информации от пользователя
    class Meta:
        model = Comments
        fields = ('name', 'email', 'text_comments')
