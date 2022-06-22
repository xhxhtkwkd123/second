from tabnanny import verbose
from django.db import models
from django.urls import reverse


from django.conf import settings
from django.contrib.auth import get_user_model
#from django.utils import timezone


# Create your models here.



class Question(models.Model):
    subject = models.CharField(max_length=100)
    content = models.TextField(max_length=1000)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = '작성글'
        verbose_name_plural = '작성글 리스트'

    def get_absolute_url(self):
        return reverse('blog:detail', args=[str(self.pk)])

    def __str__(self):
        return self.subject



class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField(max_length=1000)
    author = settings.AUTH_USER_MODEL
    created_at = models.DateTimeField(auto_now_add=True)   
    
    
    class Meta:
        verbose_name = '댓글'
        verbose_name_plural = '댓글 리스트'


    def __str__(self):
        return self.question