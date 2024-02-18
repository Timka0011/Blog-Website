from django.shortcuts import render
from .forms import CustomCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView

# Create your views here.

class CustomCreateView(CreateView):
    form_class = CustomCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')


