from django.urls import path
from .views import CustomCreateView
urlpatterns = [
    path('signup/', CustomCreateView.as_view(), name = 'signup')
]