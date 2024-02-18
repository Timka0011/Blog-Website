from django.contrib import admin
from accounts.models import CustomUser
from accounts.forms import CustomChangeForm, CustomCreationForm
from django.contrib.auth.admin import UserAdmin

# Register your models here.


class CustomUserAdmin(UserAdmin):
    add_form = CustomCreationForm
    form = CustomChangeForm
    model = CustomUser
    list_display = ("username", "number")


admin.site.register(CustomUser, CustomUserAdmin)
