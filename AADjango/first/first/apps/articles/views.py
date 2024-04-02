from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django.http import Http404
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model
from .models import Article
from .forms import ArticleForm
from .serializers import CustomUserSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from django.views import View

from django.contrib.auth.hashers import make_password
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import CustomUserSerializer
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render, redirect, get_object_or_404
from .models import Article
from .forms import ArticleForm
from django.http import Http404

import jwt
from datetime import datetime, timedelta
from django.http import JsonResponse


from django.http import HttpResponse
from. models import CustomUser
from articles.encrypt_util import *
from articles.encrypt_util import decrypt
from rest_framework_simplejwt.authentication import JWTAuthentication


def index(request):
    articles_list = Article.objects.order_by('-article_date')
    return render(request, 'articles/list.html', {'articles_list': articles_list})


def detail(request, article_id):
    try:
        a = Article.objects.get(id=article_id)
    except Article.DoesNotExist:
        raise Http404("Статья не найдена")
    
    return render(request, 'articles/detail.html', {'article': a})


def create_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = ArticleForm()

    return render(request, 'articles/create_article.html', {'form': form})

from django.shortcuts import render, redirect, get_object_or_404
from .models import Article
from .forms import ArticleForm
from django.http import Http404



def edit_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)

    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', article_id=article_id)
    else:
        form = ArticleForm(instance=article)

    return render(request, 'articles/edit_article.html', {'article': article, 'form': form})

def delete_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)

    if request.method == 'POST':
        article.delete()
        return redirect('articles:index')

    return render(request, 'articles/delete_article.html', {'article': article})

def register(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        encryptpass = encrypt(password)
        print('Original Password:', request.POST['password'])

        encryptpass= encrypt(request.POST['password'])
        print('Encrypt Password:',encryptpass)
        decryptpass= decrypt(encryptpass)
        print('Decrypt Password:',decryptpass)


        data=CustomUser(email=email, password=encryptpass)
        data.save()
        user = CustomUser.objects.get(email=email)
        payload = {
                    'user_id': user.id,
                    'exp': datetime.utcnow() + timedelta(days=1)  
                }

        token = jwt.encode(payload, 'your_secret_key', algorithm='HS256')

               
        response_data = {
                'message': 'Login Successful',
                'token': token  
            }
        
        return render(request, 'articles/list.html')
    else:
        return render(request, 'articles/index.html')
    

    
def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = CustomUser.objects.get(email=email)
            decrypted_password = decrypt(user.password)

            if decrypted_password == password:
                
                payload = {
                    'user_id': user.id,
                    'exp': datetime.utcnow() + timedelta(days=1)  
                }

                token = jwt.encode(payload, 'your_secret_key', algorithm='HS256')

               
                response_data = {
                    'message': 'Login Successful',
                    'token': token  
                }
                
                return render(request, 'articles/list.html')
            else:
                return JsonResponse({'message': 'Invalid login credentials'}, status=401)
        except CustomUser.DoesNotExist:
            return JsonResponse({'message': 'User does not exist'}, status=404)
    else:
        return render(request, 'articles/login.html')
    
