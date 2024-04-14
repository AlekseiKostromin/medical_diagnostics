from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    MALE = 'male'
    FEMALE = 'female'

    GENDER = (
        (MALE, 'мужской'),
        (FEMALE, 'женский')
    )
    username = None

    email = models.EmailField(verbose_name='почта', unique=True)
    first_name = models.CharField(max_length=50, verbose_name='имя', null=True, blank=True)
    last_name = models.CharField(max_length=50, verbose_name='фамилия', null=True, blank=True)
    phone = models.CharField(max_length=20, verbose_name='телефон', null=True, blank=True)
    age = models.IntegerField(verbose_name='возраст', null=True, blank=True)
    gender = models.IntegerField(verbose_name='пол', null=True, blank=True)
    city = models.CharField(max_length=50, verbose_name='город', null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
