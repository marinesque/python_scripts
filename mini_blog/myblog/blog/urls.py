from django.urls import path
from . import views

urlpatterns = [path('', views.PostView.as_view()),
               path('<int:pk>/', views.PostDetail.as_view())]
#Все пути до наших url адресов, пустын кавычки - главная страница
