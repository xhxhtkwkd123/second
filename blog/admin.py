from django.contrib import admin

from blog.models import Question, Answer



# Register your models here.

class QuestionAdmin(admin.ModelAdmin):
    list_display = ['subject']


class AnswerAdmin(admin.ModelAdmin):
    list_display = ['created_at']


admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
