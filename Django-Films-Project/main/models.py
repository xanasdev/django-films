from django.db import models
from django.contrib.auth.models import AbstractUser

import uuid


class Users(AbstractUser):
    userid = models.CharField(max_length=256, null=False, verbose_name='Пользовательский ID')


class Film(models.Model):
    file = models.FileField(upload_to='films/videos/')
    picture = models.FileField(upload_to='films/pictures', null=True)
    film_name = models.CharField(max_length=256, verbose_name='Название фильма')
    film_description = models.TextField(verbose_name='Описание фильма')
    film = models.CharField(max_length=256, verbose_name='Уникальный UUID4')


class Comments(models.Model):
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    comment = models.CharField(max_length=360, verbose_name='Комментарий')




