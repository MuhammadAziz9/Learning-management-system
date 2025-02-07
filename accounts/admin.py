from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm,CustomUserChangeForm
# Register your models here.

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_displey = ['username','email','degree','is_staff']
    fieldsets = UserAdmin.fieldsets + (
        (None,{'fields':('degree',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None,{'fields':('degree',)}),
    )
admin.site.register(CustomUser,CustomUserAdmin)