from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    username = None
    email = models.EmailField(verbose_name='Почта', unique=True)

    phone = models.CharField(max_length=35, verbose_name='Телефон', null=True, blank=True)
    avatar = models.ImageField(upload_to='users/', verbose_name='Изображение', null=True, blank=True)
    country = models.CharField(max_length=35, verbose_name='Страна', null=True, blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = [""]

