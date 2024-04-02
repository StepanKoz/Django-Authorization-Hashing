from django.db import models
import datetime

class Article(models.Model):
    article_tittle = models.CharField("Название статьи", max_length = 30)
    article_description = models.TextField("Текст статьи")
    article_date = models.DateTimeField("Дата публикации", default=datetime.datetime.now)

    class Meta:
        verbose_name = 'Cтатья'
        verbose_name_plural = 'Статьи'

class CustomUser(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128) 

    def __str__(self):
        return self.email
    
    class Meta:
        db_table = 'custom_user'