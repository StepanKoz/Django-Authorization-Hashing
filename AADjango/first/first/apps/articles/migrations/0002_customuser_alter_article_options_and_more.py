# Generated by Django 5.0.2 on 2024-02-21 20:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=128)),
            ],
        ),
        migrations.AlterModelOptions(
            name='article',
            options={'verbose_name': 'Cтатья', 'verbose_name_plural': 'Статьи'},
        ),
        migrations.AlterField(
            model_name='article',
            name='article_date',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='Дата публикации'),
        ),
    ]
