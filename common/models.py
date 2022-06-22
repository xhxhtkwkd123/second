from tabnanny import verbose
from django.db import models

from django.contrib.auth.models import AbstractUser

# Create your models here.

class MyUser(AbstractUser):
    nickname = models.CharField(max_length=20)


    labels = {'nickname':'닉네임',}



    class Meta:
        verbose_name = '유저정보'
        verbose_name_plural = '유저정보 리스트'
