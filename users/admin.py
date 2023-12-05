from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.hashers import make_password
from django.contrib.auth import get_user_model
from .forms import CustomUserChangeForm
from .models import *

class CustomUserAdmin(UserAdmin):
    form = CustomUserChangeForm
    model = get_user_model()

    def save_model(self, request, obj, form, change):
        password = form.cleaned_data.get('password1')
        if password:
            obj.password = make_password(password)
        super().save_model(request, obj, form, change)

admin.site.register(get_user_model(), CustomUserAdmin)


@admin.register(Honorific)
class HonorificAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Gender)
class GenderAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(MaritalStatus)
class MaritalStatusAdmin(admin.ModelAdmin):
    list_display = ('name',)
