# _*_ encoding:utf-8 _*_
from django.contrib import admin

# Register your models here.

from .models import UserProfile


# 添加users到Django管理的站点管理
class UserProfileAdmin(admin.ModelAdmin):
    pass


admin.site.register(UserProfile, UserProfileAdmin)
