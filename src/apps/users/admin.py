from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


class UserAdminConfig(UserAdmin):
    ordering = ('email',)
    list_display = ('email', 'is_superuser', 'is_staff', 'is_active')


# Register your models here.
admin.site.register(User, UserAdminConfig)