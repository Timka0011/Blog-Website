from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CustomCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ["username", "email", "number"]


class CustomChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ["username", "email", "number"]
