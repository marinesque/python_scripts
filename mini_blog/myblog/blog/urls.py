from django.urls import path
from . import views

urlpatterns = [path('', views.PostView.as_view()),
               path('<int:pk>/', views.PostDetail.as_view()),
               path('reviews/<int:pk>', views.AddComments.as_view(), name='add_comments'), #каталог для сохранения комменатриев
               path('<int:pk>/add_likes/', views.AddLike.as_view(), name='add_likes'),
               path('<int:pk>/del_likes/', views.DelLike.as_view(), name='del_likes')
               ]
#Все пути до наших url адресов, пустые кавычки - главная страница
