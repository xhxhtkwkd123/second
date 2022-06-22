from django.contrib import admin

from common.models import MyUser


# Register your models here.

class MyUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'nickname']


admin.site.register(MyUser, MyUserAdmin)

