from django.urls import path
from .views import index, detail, create_article, register, login
from . import views


app_name = 'articles'
urlpatterns = [
    path('', index, name='index'),
    path('<int:article_id>/', detail, name='detail'),
    path('create/', create_article, name='create_article'),
    path('register/', register, name='register'),
    path("login/", login, name = 'login'),
    path('<int:article_id>/delete/', views.delete_article, name='delete_article'),
    path('<int:article_id>/edit/', views.edit_article, name='edit_article'),
  
]